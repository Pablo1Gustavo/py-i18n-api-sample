from typing import Any
from fastapi.responses import JSONResponse

from ..translator import Translator
from ..selector import ContextLanguageSelector

class TranslatorResponse(JSONResponse):
    def __init__(self, content: Any, *args, **kwargs):
        current_language = ContextLanguageSelector.get_language()
        translator = Translator(current_language)
        translated_content = translator.translate_object(content)
        super().__init__(translated_content, *args, **kwargs)
