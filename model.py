from sqlmodel import Field, SQLModel
from email.policy import default
from datetime import datetime



class DogBase(SQLModel):
    name: str = Field(default=None)
    size: str = Field(default=None)
    dangerous: bool = True
    sterelized: bool = True
    breed: str = Field(default=None)
    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )
    alive: bool = True

class DogId(DogBase, table=True):
    id: int = Field(default=None, primary_key=True, gt=0)

class DogUpload(DogBase):
    id: int = Field(default = None, exclude=True)
    name: str = Field(default=None, exclude=True)
    size: str = Field(default=None)
    dangerous: bool = True
    sterelized: bool = True
    breed: str = Field(default=None)
    created: datetime = Field(default=None, exclude=True)
    alive: bool = Field(default=True, exclude=True)

