from fastapi import FastAPI, HTTPException
from model import DogBase, DogId, DogUpload
from DogOperations import createDog
from sqlmodel import Session
from sqlmodel.orm import session
from db import SessionDep, create_all_tables

app = FastAPI(lifespan=create_all_tables)




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/dog", response_model=DogId)
async def create_dog(dog: DogBase, session: SessionDep):
    return createDog(dog, session)
