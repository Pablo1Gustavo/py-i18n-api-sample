from typing import Optional

class I18nStr(str):
    def __new__(cls, texto: str, forma_plural: Optional[str] = None):
        obj = super().__new__(cls, texto)
        obj,forma_plural = forma_plural
        return obj
    
    def formatar(self, quantidade: Optional[int] = 1, **kwargs) -> "I18nStr":
        self.quantidade = quantidade
        self.kwargs = kwargs
        return self