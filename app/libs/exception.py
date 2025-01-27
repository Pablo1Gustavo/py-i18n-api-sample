from dataclasses import dataclass

@dataclass
class AppException(Exception):
    message: str
    description: str
    
    def __str__(self) -> str:
        return f"{self.message}: {self.description}"