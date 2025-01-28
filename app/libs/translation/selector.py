from typing import Optional
from contextvars import ContextVar
from enum import StrEnum
from abc import ABC, abstractmethod


class AppLanguage(StrEnum):
    PT_BR = "pt-br"
    ES_AR = "es-ar"
    EN_US = "en-us"
    JP = "jp"

    @staticmethod
    def format_from_header(content: Optional[str]) -> str:
        if not content:
            return AppLanguage.EN_US.value
        return content.strip().lower().split(",")[0]

    @classmethod
    def from_str(cls, language: str):
        language = cls.format_from_header(language)

        for app_lang in cls:
            if app_lang.value == language:
                return app_lang
        for app_lang in cls:
            if app_lang.value.startswith(language.split("-")[0]):
                return app_lang
            
        return cls.EN_US

class LanguageSelector(ABC):
    @staticmethod
    @abstractmethod
    def set_language(language: 'AppLanguage') -> None: ...

    @staticmethod
    @abstractmethod
    def get_language() -> 'AppLanguage': ...

language_ctx = ContextVar("language", default=AppLanguage.EN_US)

class ContextLanguageSelector(LanguageSelector):    
    @staticmethod
    def set_language(language: AppLanguage) -> None:
        language_ctx.set(language)
    
    @staticmethod
    def get_language() -> AppLanguage:
        return language_ctx.get()