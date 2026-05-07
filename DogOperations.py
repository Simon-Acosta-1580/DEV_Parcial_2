from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select
from sqlmodel.orm import session

from model import DogBase, DogId, DogUpload

def createDog(dog: DogBase, session: Session):
    new_dog = DogId.model_validate(dog)
    session.add(new_dog)
    session.commit()
    session.refresh(new_dog)

    return new_dog

def getAllDogs(session: Session):
    return session.query(DogBase).all()

def get_alive_dogs(session: Session):
    statement = select(DogId).where(DogId.alive == True)
    results = session.exec(statement).all()
    return results

def get_notAlive_dogs(session: Session):
    statement = select(DogId).where(DogId.activo == False)
    results = session.exec(statement).all()
    return results