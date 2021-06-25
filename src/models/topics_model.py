from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from src.database.base_class import Base

class TopicsModel(Base):
    __tablename__   = "topics"

    id           = Column(String   , nullable=False, index=True, primary_key=True)
    topic_date   = Column(DateTime , nullable=False)
    class_id     = Column(String   , ForeignKey('classes.id'), nullable=False)    
    status       = Column(String   , nullable=False, default="active")
    created_at   = Column(DateTime , nullable=False)
    updated_at   = Column(DateTime , nullable=True)