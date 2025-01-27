from typing import TypeVar, Any, Callable, Mapping, Iterator
from functools import wraps
import gettext

from .selector import LanguageSelector, AppLanguage
from .text import TranslatableStr

T = TypeVar('T')

class Translator:
    def __init__(
        self,
        language: AppLanguage,
        domain: str = "_app",
    ):
        try:
            self.translation_fn = gettext.translation(domain, "locale", [language])
        except Exception:
            print(f"Translation file not found for domain {domain} and language {language}.")
            self.translation_fn = gettext.NullTranslations()

    def translate(self, text: TranslatableStr) -> str:
        if text.plural_form:
            translated =  self.translation_fn.ngettext(text, text.plural_form, text.amount)
        else:
            translated = self.translation_fn.gettext(text)
        return translated.format(*text.args, **text.kwargs)
    
    def translate_object(self, obj: T) -> T:
        if isinstance(obj, TranslatableStr):
            return self.translate(obj)
        if isinstance(obj, Mapping):
            return {
                self.translate_object(key): self.translate_object(value)
                for key, value in obj.items()
            }
        if isinstance(obj, Iterator) and not isinstance(obj, str):
            return [self.translate_object(item) for item in obj]
        return obj

def translate_return(fn: Callable) -> Callable:
    @wraps(fn)
    async def wrapper(*args, **kwargs) -> Any:
        current_language = LanguageSelector.get_language()
        translator = Translator(current_language)
        try:
            original_return = await fn(*args, **kwargs)
        except Exception as e:
            e.message = translator.translate(e.message)
            e.description = translator.translate(e.description)
            raise e
        return translator.translate_object(original_return)
    
    return wrapper