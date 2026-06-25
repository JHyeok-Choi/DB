from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate
from schemas import UserUpdate


def create_user(
    db: Session,
    payload: UserCreate,
) -> User:

    user = User(
        name=payload.name,
        email=payload.email,
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user(
    db: Session,
    user_id: int,
) -> User | None:

    stmt = select(User).where(
        User.id == user_id
    )

    return db.scalar(stmt)

def get_users(
    db: Session,
    skip: int = 0,
    limit: int = 100,
) -> list[User]:

    stmt = (
        select(User)
        .offset(skip)
        .limit(limit)
    )

    return list(
        db.scalars(stmt).all()
    )

def update_user(
    db: Session,
    user_id: int,
    payload: UserUpdate,
) -> User | None:

    stmt = select(User).where(
        User.id == user_id
    )

    user = db.scalar(stmt)

    if user is None:
        return None

    user.name = payload.name

    db.commit()

    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int,
) -> bool:

    stmt = select(User).where(
        User.id == user_id
    )

    user = db.scalar(stmt)

    if user is None:
        return False

    db.delete(user)

    db.commit()

    return True
