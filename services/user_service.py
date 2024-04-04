from sqlalchemy.orm import Session
from models.User import User
from DTO.response.User_response_DTO import CreateUserSchema

def create_user(session: Session,user: CreateUserSchema):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, login:str):
    return session.query(User).filter(User.login == login).one()

def get_user_by_id(session:Session,id: int):
    return session.query(User).filter(User.id == id).one()