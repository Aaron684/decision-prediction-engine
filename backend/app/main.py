from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.routers.categories import router as category_router
from app.routers.features import router as feature_router
from app.routers.observations import router as observation_router
from app.routers.training import router as training_router
from app.database.database import engine
from app.database.base import Base

from app.api.prediction import router as prediction_router

from app.models import *

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(feature_router)
app.include_router(observation_router)
app.include_router(prediction_router)
app.include_router(training_router)

@app.get("/")
def root():
    return {"message": "Decision Prediction Engine API"}