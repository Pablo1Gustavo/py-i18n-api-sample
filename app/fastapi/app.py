

from typing import Callable
from fastapi import FastAPI, Request

from app.libs.exception import AppException
from app.libs.translation.selector import AppLanguage, ContextLanguageSelector
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
    client_lang = AppLanguage.from_str(request.headers.get("Accept-Language"))
    ContextLanguageSelector.set_language(client_lang)
    return await call_next(request)

@app.exception_handler(AppException)
def app_exception_handler(request: Request, e: AppException):
    return TranslatorResponse({
        "message": e.message,
        "description": e.description
    }, 400)

@app.get("/test")
async def test():
    return "Server is running on port 8080"
