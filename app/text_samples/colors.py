from dataclasses import dataclass

@dataclass
class RedColorException(Exception):
    message: str = "Red is not a valid color"
    description: str = "Red is a primary color"

class Color:
    def __init__(self, name: str, hex_code: str):
        self.name = name
        self.hex_code = hex_code

color_item = Color("Pink", "#0000FF")

def get_colors() -> list[str]:
    return [
        "Red",
        "Green",
        "Blue",
        "Yellow",
        "Orange",
        "Purple",
    ]

def dont_get_red(color: str) -> str:
    if color == "Red":
        raise RedColorException()
    return color

def get_hex_to_colors_map() -> dict[str, str]:
    return {
        "#FF0000": "Red",
        "#00FF00": "Green",
        "#0000FF": "Blue",
        "#FFFF00": "Yellow",
        "#FFA500": "Orange",
        "#800080": "Purple",
    }

def write_color_poem() -> str:
    poem = "Rose are red, violets are blue..."
    return poem
