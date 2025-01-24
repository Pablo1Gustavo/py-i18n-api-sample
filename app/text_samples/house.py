from dataclasses import dataclass

@dataclass
class HouseItemException(Exception):
    message: str = "This house item is not allowed"
    description: str = "The requested house item is either prohibited or unavailable"

class HouseItem:
    def __init__(self, name: str, material: str):
        self.name = name
        self.material = material

house_item = HouseItem("Chair", "Wood")

def get_house_items() -> list[str]:
    return [
        "Table",
        "Chair",
        "Lamp",
        "Sofa",
        "Bed",
        "Bookshelf",
    ]

def dont_allow_lamp(item: str) -> str:
    if item == "Lamp":
        raise HouseItemException(
            message="Lamps are currently restricted",
            description="Please select another item"
        )
    return item

def get_item_to_material_map() -> dict[str, str]:
    return {
        "Table": "Wood",
        "Chair": "Wood",
        "Lamp": "Metal",
        "Sofa": "Fabric",
        "Bed": "Wood",
        "Bookshelf": "Wood",
    }

def write_house_poem() -> str:
    poem = "A chair to sit, a bed for dreams,\nA lamp to light, and books on beams."
    return poem
