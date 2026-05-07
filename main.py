from fastapi import FastAPI, HTTPException
from model import DogBase, DogId, DogUpload
from DogOperations import createDog, get_alive_dogs, get_notAlive_dogs, find_one_dogs, update_one_dog, delete_dog
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

@app.get("/dogs", response_model=list[DogId])
async def show_dogs(session: SessionDep):
    alive = get_alive_dogs(session)
    if not alive:
        raise HTTPException(status_code=404, detail="No dogs")
    return alive

@app.get("/dogsNotAlive", response_model=list[DogId])
async def show_notAlive_dogs(session: SessionDep):
    notAlive = get_notAlive_dogs(session)
    if not notAlive:
        raise HTTPException(status_code=404, detail="No not alive dogs")
    return notAlive

@app.get("/dog/{id}", response_model=DogId)
async def show_one_dog(id: int, session: SessionDep):
    dog = find_one_dogs(id, session)
    if not (dog):
        raise HTTPException(status_code=404, detail=f"{id} dog not found")
    return dog

@app.patch("/dog/{id}", response_model=DogId, response_model_exclude={"id", "nombre", "created", "alive"})
async def update_dog(id: int, dog: DogUpload, session: SessionDep):
    update = update_one_dog(id, dog, session)
    if not (update):
        raise HTTPException(status_code=404, detail=f"{id} dog not found")
    return update

@app.delete("/dog/{id}", response_model=DogId)
async def delete_one_dog(id: int, session: SessionDep):
    eliminado = delete_dog(id, session)

    if not eliminado:
        raise HTTPException(status_code=404, detail=f"dog {id} no encontrado")

    return eliminado