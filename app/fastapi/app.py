

from typing import Callable
from fastapi import FastAPI, Request

from app.libs.translation.selector import LanguageSelector
from app.libs.translation.fastapi.translator_response import TranslatorResponse

from .colors_router import router as colors_router
from .foods_router import router as foods_router
from .house_router import router as house_router


app = FastAPI(default_response_class=TranslatorResponse)

app.include_router(colors_router)
app.include_router(foods_router)
app.include_router(house_router)
    
@app.middleware("http")
async def apply_language(request: Request, call_next: Callable):
    client_lang = LanguageSelector.get_from_header(request.headers.get("Accept-Language"))
    LanguageSelector.set_language(client_lang)
    return await call_next(request)


@app.get("/test")
async def test():
    return "Server is running on port 8080"
