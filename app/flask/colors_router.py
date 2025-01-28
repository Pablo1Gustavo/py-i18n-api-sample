from flask import Blueprint 

from app.text_samples.colors import (
    color_item,
    get_colors,
    get_hex_to_colors_map,
    dont_get_red,
    write_color_poem
)

colors = Blueprint("colors", __name__, url_prefix="/colors")

@colors.route("/", methods=['GET'])
async def food_items():
    return get_colors()

@colors.route("/item", methods=['GET'])
async def color_class():
    return {
        "name": color_item.name,
        "hex_code": color_item.hex_code
    }

@colors.route("/hex", methods=['GET'])
async def hex_colors():
    return get_hex_to_colors_map()

@colors.route("/try/<color>", methods=['GET'])
async def try_get_color(color: str):
    return dont_get_red(color)

@colors.route("/poem", methods=['GET'])
async def color_poem():
    return write_color_poem()