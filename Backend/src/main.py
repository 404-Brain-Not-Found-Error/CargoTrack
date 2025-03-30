from fastapi import FastAPI

from config import settings


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)
