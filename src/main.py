from fastapi import FastAPI
from .auth.routers import router as auth_router
from .file_loader.routers import router as file_router
from .cards.routers import router as card_router


app = FastAPI()
app.include_router(auth_router, prefix='/auth')
app.include_router(file_router)
app.include_router(card_router)
