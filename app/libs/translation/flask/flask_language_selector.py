from flask import g

from ..selector import AppLanguage, LanguageSelector

class FlaskLanguageSelector(LanguageSelector):
    @staticmethod
    def set_language(language: AppLanguage):
        g.language = language

    @staticmethod
    def get_language():
        return g.language