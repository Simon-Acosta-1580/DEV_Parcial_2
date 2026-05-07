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

