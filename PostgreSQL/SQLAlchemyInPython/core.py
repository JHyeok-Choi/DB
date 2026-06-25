from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# Primary (쓰기)
WRITE_DATABASE_URL = (
    "postgresql://test:test"
    "@localhost:5432/testdb"
)

# Replica (읽기)
READ_DATABASE_URL = (
    "postgresql://test:test"
    "@localhost:5432/testdb"
)

# Engine 생성
write_engine = create_engine(
    WRITE_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=40,
)

read_engine = create_engine(
    READ_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=40,
)

# Session Factory
WriteSessionLocal = sessionmaker(
    bind=write_engine,
    autocommit=False,
    autoflush=False,
)

ReadSessionLocal = sessionmaker(
    bind=read_engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def get_write_db():
    """
    INSERT
    UPDATE
    DELETE

    생성 직후 조회
    수정 직후 조회
    """

    db = WriteSessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_read_db():
    """
    일반 조회

    Replica 사용
    """

    db = ReadSessionLocal()

    try:
        yield db

    finally:
        db.close()
