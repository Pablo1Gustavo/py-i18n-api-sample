from flask.json.provider import DefaultJSONProvider

from ..translator import Translator
from .flask_language_selector import FlaskLanguageSelector

class TranslatorJSONProvider(DefaultJSONProvider):    
    def dumps(self, o: object, **kwargs):
        current_language = FlaskLanguageSelector.get_language()
        translator = Translator(current_language)
        translated_content = translator.translate_object(o)
        return super().dumps(translated_content, **kwargs)