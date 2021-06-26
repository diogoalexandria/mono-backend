from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from src.database.base_class import Base

class SubjectsModel(Base):
    __tablename__   = "subjects"

    id         = Column(String   , nullable=False, index=True, primary_key=True)
    name       = Column(String   , nullable=False, index=True, unique=True)
    status     = Column(String   , nullable=False, default="active")
    created_at = Column(DateTime , nullable=False)
    updated_at = Column(DateTime , nullable=True)
    classes    = relationship('ClassesModel', cascade='all,delete', backref='subjects')
    # registries = relationship('Registries', cascade='all,delete', backref='subjects')