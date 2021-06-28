from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from src.database.base_class import Base

class AttendancesModel(Base):
    __tablename__   = "attendances"

    id           = Column(String   , nullable=False, index=True, primary_key=True)
    topic_id     = Column(String   , ForeignKey('topics.id'), nullable=False)
    student_id   = Column(String   , ForeignKey('users.id'), nullable=False)    
    created_at   = Column(DateTime , nullable=False)
    updated_at   = Column(DateTime , nullable=True)
    # subscriptions   = relationship('SubscriptionsModel', cascade='all,delete', backref='users')