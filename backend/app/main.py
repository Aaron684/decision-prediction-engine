from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers.categories import router as category_router
from app.routers.features import router as feature_router
from app.routers.observations import router as observation_router

from app.database.database import engine
from app.database.base import Base

from app.models import *


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(category_router)
app.include_router(feature_router)
app.include_router(observation_router)


@app.get("/")
def root():
    return {"message": "Decision Prediction Engine API"}