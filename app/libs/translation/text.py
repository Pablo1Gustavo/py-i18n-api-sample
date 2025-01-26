from typing import Optional

from .selector import LanguageSelector

# lazy translation (response time)
class TranslatableStr(str):
    def __new__(cls, text: str, plural_form: Optional[str] = None):
        obj = super().__new__(cls, text)
        obj.plural_form = plural_form
        obj.args = (),
        obj.kwargs = {}
        return obj
    
    def format(self, *args, **kwargs) -> "TranslatableStr":
        self.args = args
        self.kwargs = kwargs
        return self

# eager translation (startup time)
class StrWithTranslation(TranslatableStr):
    def __new__(
        cls,
        text: str,
        plural_form: Optional[str] = None,
        *args,
        **kwargs
    ):
        from .translator import Translator

        obj = super().__new__(cls, text, plural_form)
        obj = obj.format(*args, **kwargs)

        print(LanguageSelector.get_language())

        translator = Translator(LanguageSelector.get_language())

        return translator.translate(obj)