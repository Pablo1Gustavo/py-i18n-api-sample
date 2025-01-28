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
        domains: list[str] = ["_app"],
    ):
        self.translation_fn = gettext.NullTranslations()
        for domain in domains:
            try:
                translation = gettext.translation(
                    domain,
                    localedir="locale",
                    languages=[language.value],
                )
                self.translation_fn.add_fallback(translation)
            except FileNotFoundError as e:
                print(f"Translation file not found for domain {e.filename} and language {language}.")

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

def translate_return(
    language_selector: LanguageSelector,
    domains: list[str] = ["_app"]
) -> Callable:
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        async def wrapper(*args, **kwargs) -> Any:
            current_language = language_selector.get_language()
            translator = Translator(current_language, domains)
            try:
                original_return = await fn(*args, **kwargs)
            except Exception as e:
                e.message = translator.translate(e.message)
                e.description = translator.translate(e.description)
                raise e
            return translator.translate_object(original_return)
        return wrapper
    return decorator
