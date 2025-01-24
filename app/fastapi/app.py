from fastapi import FastAPI

from .colors_router import router as colors_router
from .foods_router import router as foods_router
from .house_router import router as house_router

app = FastAPI()

app.include_router(colors_router)
app.include_router(foods_router)
app.include_router(house_router)

@app.get("/test")
async def test():
    return "Server is running on port 8080"
