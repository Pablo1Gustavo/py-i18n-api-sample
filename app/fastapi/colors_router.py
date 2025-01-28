from fastapi import APIRouter 

from app.text_samples.colors import (
    color_item,
    get_colors,
    get_hex_to_colors_map,
    dont_get_red,
    write_color_poem
)

router = APIRouter(prefix="/colors")

@router.get("/")
async def food_items():
    return get_colors()

@router.get("/item")
async def color_class():
    return {
        "name": color_item.name,
        "hex_code": color_item.hex_code
    }

@router.get("/hex")
async def hex_colors():
    return get_hex_to_colors_map()

@router.get("/try/{color}")
async def try_get_color(color: str):
    return dont_get_red(color)

@router.get("/poem")
async def color_poem():
    return write_color_poem()