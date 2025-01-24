from dataclasses import dataclass

@dataclass
class FoodException(Exception):
    message: str = "This food item is not available"
    description: str = "The requested food is currently unavailable or restricted"

class Food:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

food_item = Food("Pizza", 285)

def get_food_items() -> list[str]:
    return [
        "Pizza",
        "Burger",
        "Pasta",
        "Salad",
        "Sushi",
        "Tacos",
    ]

def dont_serve_sushi(food: str) -> str:
    if food == "Sushi":
        raise FoodException(
            message="Sushi is not served today",
            description="Try other items on the menu"
        )
    return food

def get_food_to_calories_map() -> dict[str, int]:
    return {
        "Pizza": 285,
        "Burger": 354,
        "Pasta": 221,
        "Salad": 152,
        "Sushi": 200,
        "Tacos": 156,
    }

def write_food_poem() -> str:
    poem = "Pizza is round, tacos are folded,\nBurgers are tasty, pasta is golden."
    return poem
