from dataclasses import dataclass

from app.libs.exception import AppException
from app.libs.translation.text import TranslatableStr

@dataclass
class FoodException(AppException):
    message: str = TranslatableStr("This food item is not available")
    description: str = TranslatableStr("The requested food is currently unavailable or restricted")

class Food:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

food_item = Food(TranslatableStr("Pizza"), 285)

def get_food_items() -> list[str]:
    return [
        TranslatableStr("Pizza"),
        TranslatableStr("Burger"),
        TranslatableStr("Pasta"),
        TranslatableStr("Salad"),
        TranslatableStr("Sushi"),
        TranslatableStr("Tacos"),
    ]

def dont_serve_sushi(food: str) -> str:
    if food.lower() == "sushi":
        raise FoodException()
    return TranslatableStr("You ordered {food}").format(food=food)

def get_food_to_calories_map() -> dict[str, int]:
    return {
        TranslatableStr("Pizza"): 285,
        TranslatableStr("Burger"): 354,
        TranslatableStr("Pasta"): 221,
        TranslatableStr("Salad"): 152,
        TranslatableStr("Sushi"): 200,
        TranslatableStr("Tacos"): 156,
    }

def write_food_poem() -> str:
    poem = TranslatableStr("Pizza is round, tacos are folded,\nBurgers are tasty, pasta is golden.")
    return poem
