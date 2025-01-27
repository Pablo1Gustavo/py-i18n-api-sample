from typing import Optional
from contextvars import ContextVar
from enum import StrEnum

class AppLanguage(StrEnum):
    PT_BR = "pt-br"
    ES_AR = "es-ar"
    JP = "jp"
    EN = "en"

    @classmethod
    def from_str(cls, language: str):
        for app_lang in cls:
            if app_lang.value == language:
                return app_lang
        for app_lang in cls:
            if app_lang.value.startswith(language.split("-")[0]):
                return app_lang
        return cls.EN

language_ctx = ContextVar("language", default=AppLanguage.EN)

class LanguageSelector():
    @staticmethod
    def get_from_header(content: Optional[str]) -> AppLanguage:
        if not content:
            return AppLanguage.EN
        content_lang = content.strip().lower().split(",")[0]
        return AppLanguage.from_str(content_lang)
    
    @staticmethod
    def set_language(language: AppLanguage) -> None:
        language_ctx.set(language)
    
    @staticmethod
    def get_language() -> AppLanguage:
        return language_ctx.get()