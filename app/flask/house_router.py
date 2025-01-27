from flask import Blueprint

from app.text_samples.house import (
    house_item,
    get_house_items,
    get_item_to_material_map,
    dont_allow_lamp,
    write_house_poem
)

house = Blueprint("house", __name__, url_prefix="/house")

@house.route("/", methods=['GET'])
async def house_items():
    return get_house_items()

@house.route("/item", methods=['GET'])
async def house_item_details():
    return {
        "name": house_item.name,
        "material": house_item.material
    }

@house.route("/materials", methods=['GET'])
async def item_materials():
    return get_item_to_material_map()

@house.route("/try/{item}", methods=['GET'])
async def try_get_item(item: str):
    return dont_allow_lamp(item)

@house.route("/poem", methods=['GET'])
async def house_item_poem():
    return write_house_poem()
