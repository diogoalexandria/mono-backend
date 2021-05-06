from typing import Generator
from conn import SessionLocal

def db_session() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
