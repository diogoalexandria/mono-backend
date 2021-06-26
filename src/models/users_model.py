from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database.base_class import Base

class UsersModel(Base):
    __tablename__   = "users"

    id              = Column(String   , nullable=False, index=True, primary_key=True)
    email           = Column(String   , nullable=False, index=True, unique=True)
    username        = Column(String   , nullable=False, index=True, unique=True)
    first_name      = Column(String   , nullable=False)
    last_name       = Column(String   , nullable=False)    
    password        = Column(String   , nullable=False)
    entity          = Column(String   , nullable=False)
    gender          = Column(String   , nullable=True)
    status          = Column(String   , nullable=False, default="active")
    course_id       = Column(String   , ForeignKey('courses.id'), nullable=True)
    created_at      = Column(DateTime , nullable=False)
    updated_at      = Column(DateTime , nullable=True)
    subscriptions   = relationship('SubscriptionsModel', cascade='all,delete', backref='users')
    # attendances   = relationship('AttendancesModel', cascade='all,delete', backref='users')
