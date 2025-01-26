from dataclasses import dataclass

from app.libs.translation.text import TranslatableStr

@dataclass
class RedColorException(Exception):
    message: str = TranslatableStr("Red is not a valid color")
    description: str = TranslatableStr("Red is a primary color")

class Color:
    def __init__(self, name: str, hex_code: str):
        self.name = name
        self.hex_code = hex_code

color_item = Color(TranslatableStr("Pink"), "#0000FF")

def get_colors() -> list[str]:
    return [
        TranslatableStr("Red"),
        TranslatableStr("Blue"),
        TranslatableStr("Yellow"),
        TranslatableStr("Orange"),
        TranslatableStr("Purple"),
    ]

def dont_get_red(color: str) -> str:
    if color.lower() == "red":
        raise RedColorException()
    return color

def get_hex_to_colors_map() -> dict[str, str]:
    return {
        "#FF0000": TranslatableStr("Red"),
        "#00FF00": TranslatableStr("Green"),
        "#0000FF": TranslatableStr("Blue"),
        "#FFFF00": TranslatableStr("Yellow"),
        "#FFA500": TranslatableStr("Orange"),
        "#800080": TranslatableStr("Purple"),
    }

def write_color_poem() -> str:
    poem = TranslatableStr("Rose are red, violets are blue...")
    return poem
