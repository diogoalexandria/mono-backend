from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from src.database.base_class import Base

class SubscriptionsModel(Base):
    __tablename__   = "subscriptions"

    id           = Column(String   , nullable=False, index=True, primary_key=True)    
    class_id     = Column(String   , ForeignKey('classes.id'), nullable=False)
    student_id   = Column(String   , ForeignKey('users.id'), nullable=True)
    status       = Column(String   , nullable=False, default="active")
    created_at   = Column(DateTime , nullable=False)
    updated_at   = Column(DateTime , nullable=True)