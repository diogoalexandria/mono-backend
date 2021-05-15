import uuid
from typing import Optional
from datetime import datetime
from sqlalchemy.orm import Session 
from src.helpers.auth import Auth
from src.models.user_model import UserModel
from src.schemas.users_schemas import UserRequestSchema, UserUpdateSchema
from src.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[UserModel, UserRequestSchema, UserUpdateSchema]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.email == email).first()
        
    def get_by_username(self, db: Session, *, username: str):
        return db.query(UserModel).filter(UserModel.username == username).first()

    def create(self, db: Session, *, req_object: UserRequestSchema) -> UserModel:
        db_object = UserModel(
            id=uuid.uuid4(),
            email=req_object.email,
            username=req_object.username,
            first_name=req_object.first_name,
            last_name=req_object.last_name,
            entity=req_object.entity,
            gender=req_object.gender,
            password=Auth.hash_password(req_object.password),
            status='active',
            created_at=datetime.utcnow()
        )

        db.add(db_object)
        db.commit()
        db.refresh(db_object)

        return db_object

    def update():
        pass       


UserRepository = UserRepository(UserModel)