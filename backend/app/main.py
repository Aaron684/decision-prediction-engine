from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

from app.models import *


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Decision Prediction Engine API"}