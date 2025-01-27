from flask import Blueprint

from app.text_samples.foods import (
    food_item,
    get_food_items,
    get_food_to_calories_map,
    dont_serve_sushi,
    write_food_poem
)

foods = Blueprint("foods", __name__, url_prefix="/foods")

@foods.route("/", methods=['GET'])
async def food_items():
    return get_food_items()

@foods.route("/item", methods=['GET'])
async def food_item_details():
    return {
        "name": food_item.name,
        "calories": food_item.calories
    }

@foods.route("/calories", methods=['GET'])
async def food_calories():
    return get_food_to_calories_map()

@foods.route("/try/{food}", methods=['GET'])
async def try_get_food(food: str):
    return dont_serve_sushi(food)

@foods.route("/poem", methods=['GET'])
async def food_poem():
    return write_food_poem()
