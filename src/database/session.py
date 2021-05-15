from typing import Generator
from src.database.conn import SessionLocal

def db_session() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
