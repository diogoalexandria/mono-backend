import os
#import databases
#import sqlalchemy

from sqlalchemy.orm import sessionmaker
DATABASE_URL = os.environ['DATABASE_URL']

#database = databases.Database( DATABASE_URL )
#metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine( DATABASE_URL )
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
#metadata.create_all(engine)
