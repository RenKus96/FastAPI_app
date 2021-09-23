from sqlalchemy.orm import Session

from models import User, users
import schemas


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_password(db: Session, id: int, password: str):
    query = users.update().where(id == users.c.id)\
        .values(password = password)\
        .returning(users.c.id)
    result = db.execute(query)
    db.commit()
    return result


def update_user(db: Session, id: int, user: schemas.UserUpdate):
    query = users.update().where(users.c.id == id)\
        .values(**user.dict())
    result = db.execute(query)
    db.commit()
    return result


def delete_user(db: Session, id: int):
    query = users.delete().where(id == users.c.id)
    result = db.execute(query)
    db.commit()
    return result
