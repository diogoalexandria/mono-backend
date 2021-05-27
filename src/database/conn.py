import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
DATABASE_URL = os.environ['DATABASE_URL']

engine = sqlalchemy.create_engine( DATABASE_URL )
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
