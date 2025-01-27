from dataclasses import dataclass

from app.libs.exception import AppException
from app.libs.translation.text import TranslatableStr

@dataclass
class HouseItemException(AppException):
    message: str = TranslatableStr("This house item is not allowed")
    description: str = TranslatableStr("The requested house item is either prohibited or unavailable")

class HouseItem:
    def __init__(self, name: str, material: str):
        self.name = name
        self.material = material

house_item = HouseItem(TranslatableStr("Chair"), ("Wood"))

def get_house_items() -> list[str]:
    return [
        TranslatableStr("Table"),
        TranslatableStr("Chair"),
        TranslatableStr("Lamp"),
        TranslatableStr("Sofa"),
        TranslatableStr("Bed"),
        TranslatableStr("Bookshelf"),
    ]

def dont_allow_lamp(item: str) -> str:
    if item.lower() == "lamp":
        raise HouseItemException()
    return TranslatableStr("You ordered {item}").format(item=item)

def get_item_to_material_map() -> dict[str, str]:
    return {
        TranslatableStr("Table"): TranslatableStr("Wood"),
        TranslatableStr("Chair"): TranslatableStr("Wood"),
        TranslatableStr("Lamp"): TranslatableStr("Metal"),
        TranslatableStr("Sofa"): TranslatableStr("Fabric"),
        TranslatableStr("Bed"): TranslatableStr("Wood"),
        TranslatableStr("Bookshelf"): TranslatableStr("Wood"),
    }

def write_house_poem() -> str:
    poem = TranslatableStr("A chair to sit, a bed for dreams,\nA lamp to light, and books on beams.")
    return poem
