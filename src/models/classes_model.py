from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from src.database.base_class import Base

class ClassesModel(Base):
    __tablename__   = "classes"

    id            = Column(String   , nullable=False, index=True, primary_key=True)
    name          = Column(String   , nullable=False, index=True, unique=True)
    status        = Column(String   , nullable=False, default="active")
    subject_id    = Column(String   , ForeignKey('subjects.id'), nullable=False)
    professor_id  = Column(String   , ForeignKey('users.id'), nullable=True)
    created_at    = Column(DateTime , nullable=False)
    updated_at    = Column(DateTime , nullable=True)
    topics        = relationship('TopicsModel', cascade='all,delete', backref='classes')
    subscriptions = relationship('SubscriptionsModel', cascade='all,delete', backref='classes')