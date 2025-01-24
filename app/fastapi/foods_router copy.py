from fastapi import APIRouter

from app.text_samples.foods import (
    food_item,
    get_food_items,
    get_food_to_calories_map,
    dont_serve_sushi,
    write_food_poem
)

router = APIRouter(prefix="/foods")

@router.get("/")
async def food_items():
    return get_food_items()

@router.get("/item")
async def food_item_details():
    return {
        "name": food_item.name,
        "calories": food_item.calories
    }

@router.get("/calories")
async def food_calories():
    return get_food_to_calories_map()

@router.get("/try/{food}")
async def try_get_food(food: str):
    return dont_serve_sushi(food)

@router.get("/poem")
async def food_poem():
    return write_food_poem()
