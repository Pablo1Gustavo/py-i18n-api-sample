from typing import Optional
from .translator import global_translator

class TranslatableStr(str):
    def __new__(cls, text: str, plural_form: Optional[str] = None):
        obj = super().__new__(cls, text)
        obj.plural_form = plural_form
        return obj
    
    def format(self, *args, **kwargs) -> "TranslatableStr":
        self.args = args
        self.kwargs = kwargs
        return self
    
class StrWithTranslation(TranslatableStr):
    def __new__(
        cls,
        text: str,
        plural_form: Optional[str] = None,
        *args,
        **kwargs
    ):        
        obj = super().__new__(cls, text, plural_form)
        obj.format(*args, **kwargs)

        return global_translator.translate(obj)