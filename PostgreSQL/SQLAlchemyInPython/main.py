from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from sqlalchemy.orm import Session

from core import Base
from core import write_engine

from core import get_write_db
from core import get_read_db

from schemas import UserCreate
from schemas import UserUpdate
from schemas import UserResponse

from crud import create_user
from crud import get_user
from crud import get_users
from crud import update_user
from crud import delete_user


Base.metadata.create_all(
    bind=write_engine
)

app = FastAPI()


# ------------------------
# CREATE
# ------------------------
@app.post(
    "/users",
    response_model=UserResponse,
)
def create_user_api(
    payload: UserCreate,
    db: Session = Depends(get_write_db),
):

    return create_user(
        db=db,
        payload=payload,
    )


# ------------------------
# READ (Replica)
# ------------------------
@app.get(
    "/users/{user_id}",
    response_model=UserResponse,
)
def get_user_api(
    user_id: int,
    db: Session = Depends(get_read_db),
):

    user = get_user(
        db=db,
        user_id=user_id,
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user

@app.get(
    "/users",
    response_model=list[UserResponse],
)
def get_users_api(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_read_db),
):

    return get_users(
        db=db,
        skip=skip,
        limit=limit,
    )

# ------------------------
# READ (Primary)
#
# 생성 직후 조회용
# ------------------------
@app.get(
    "/users/{user_id}/consistent",
    response_model=UserResponse,
)
def get_user_consistent_api(
    user_id: int,
    db: Session = Depends(get_write_db),
):

    user = get_user(
        db=db,
        user_id=user_id,
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user

@app.get(
    "/users/consistent",
    response_model=list[UserResponse],
)
def get_users_api(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_write_db),
):

    return get_users(
        db=db,
        skip=skip,
        limit=limit,
    )

@app.get(
    "/users",
    response_model=list[UserResponse],
)
def get_users_api(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_read_db),
):

    return get_users(
        db=db,
        skip=skip,
        limit=limit,
    )

# ------------------------
# UPDATE
# ------------------------
@app.put(
    "/users/{user_id}",
    response_model=UserResponse,
)
def update_user_api(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_write_db),
):

    user = update_user(
        db=db,
        user_id=user_id,
        payload=payload,
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user


# ------------------------
# DELETE
# ------------------------
@app.delete(
    "/users/{user_id}",
)
def delete_user_api(
    user_id: int,
    db: Session = Depends(get_write_db),
):

    success = delete_user(
        db=db,
        user_id=user_id,
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "success": True,
    }
