from fastapi import APIRouter

from app.text_samples.house import (
    house_item,
    get_house_items,
    get_item_to_material_map,
    dont_allow_lamp,
    write_house_poem
)

router = APIRouter(prefix="/house")

@router.get("/")
async def house_items():
    return get_house_items()

@router.get("/item")
async def house_item_details():
    return {
        "name": house_item.name,
        "material": house_item.material
    }

@router.get("/materials")
async def item_materials():
    return get_item_to_material_map()

@router.get("/try/{item}")
async def try_get_item(item: str):
    return dont_allow_lamp(item)

@router.get("/poem")
async def house_item_poem():
    return write_house_poem()
