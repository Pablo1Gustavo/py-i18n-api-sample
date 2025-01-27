from typing import Any
from fastapi import Request
from fastapi.responses import JSONResponse

from app.libs.exception import AppException
from ..translator import Translator
from ..selector import LanguageSelector

class TranslatorResponse(JSONResponse):
    def __init__(self, content: Any, *args, **kwargs):
        current_language = LanguageSelector.get_language()
        translator = Translator(current_language)
        translated_content = translator.translate_object(content)
        super().__init__(translated_content, *args, **kwargs)


def app_exception_handler(request: Request, e: AppException):
    return TranslatorResponse({
        "message": e.message,
        "description": e.description
    }, 400)