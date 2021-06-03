from sqlalchemy import Column, String, DateTime
from src.database.base_class import Base

class SubjectsModel(Base):
    __tablename__   = "subjects"

    id         = Column(String   , nullable=False, index=True, primary_key=True)
    name       = Column(String   , nullable=False, index=True, unique=True)
    created_at = Column(DateTime , nullable=False)
    updated_at = Column(DateTime , nullable=True)
    