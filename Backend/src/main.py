from fastapi import FastAPI

from core.config import settings
from routes.users import router as user_router


app = FastAPI(
    title=settings.app_name,
    debug=settings.app_debug,
)
app.include_router(user_router)
