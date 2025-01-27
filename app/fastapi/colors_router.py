from fastapi import APIRouter 

from app.text_samples.colors import (
    color_item,
    get_colors,
    get_hex_to_colors_map,
    dont_get_red,
    write_color_poem
)

router = APIRouter(prefix="/colors")

@router.route("/")
async def food_items():
    return get_colors()

@router.route("/item")
async def color_class():
    return {
        "name": color_item.name,
        "hex_code": color_item.hex_code
    }

@router.route("/hex")
async def hex_colors():
    return get_hex_to_colors_map()

@router.route("/try/{color}")
async def try_get_color(color: str):
    return dont_get_red(color)

@router.route("/poem")
async def color_poem():
    return write_color_poem()