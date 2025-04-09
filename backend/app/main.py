import logging

from fastapi import FastAPI
from app.routes.auth import auth_router

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG for detailed logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app.include_router(auth_router, prefix="/api")