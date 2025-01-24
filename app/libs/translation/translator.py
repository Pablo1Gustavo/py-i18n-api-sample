from typing import Mapping, Any
import gettext

from .text import TranslatableStr

class Translator:
    def __init__(
        self,
        languages: list[str],
        domain: str = "_app",
    ):
        try:
            self.translation_fn = gettext.translation(domain, "locale", languages)
        except Exception:
            print("Translation file not found.")
            self.translation_fn = gettext.NullTranslations()

    def translate(self, text: TranslatableStr) -> str:
        if text.plural_form:
            translated =  self.translation_fn.ngettext(text, text.plural_form, text.amount)
        else:
            translated = self.translation_fn.gettext(text)
        return translated.format(*text.args, **text.kwargs)
    
    def translate_object(self, obj: object) -> Any:
        match obj:
            case TranslatableStr():
                return self.translate(obj)
            case Mapping():
                return { key: self.translate_object(value) for key, value in obj.items() }
            case list():
                return [self.translate_object(item) for item in obj]
            case tuple():
                return tuple(self.translate_object(item) for item in obj)
            case _:
                return obj
            
global_translator = Translator(["pt-BR"])