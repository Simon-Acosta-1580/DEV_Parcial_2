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

def find_one_dogs(id: int, session: Session):
    try:
        return session.get_one(DogId, id)
    except NoResultFound:
        return None

def update_one_dog(id: int, new_dog: DogUpload, session: Session):
    dog = session.get(DogId, id)

    if not dog:
        return None

    try:
        update_data = new_dog.model_dump(exclude_unset=True)

        dog.sqlmodel_update(update_data)

        session.add(dog)
        session.commit()
        session.refresh(dog)
        return dog

    except Exception as e:
        return None

def delete_dog(id: int, session: Session):
    dog = session.get(DogId, id)

    if not dog:
        return None

    dog.alive = False

    session.add(dog)
    session.commit()
    session.refresh(dog)

    return dog