from sqlmodel import SQLModel, create_engine, Session
from app.config.env import DATABASE_URL
from typing import Annotated
from fastapi import Depends

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(bind=engine)

def get_db():
    with Session(engine) as session:
        yield session

db_dependency = Annotated[Session, Depends(get_db)]