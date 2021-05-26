import uuid
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Session 
from src.helpers.auth import Auth
from src.models.user_model import UserModel
from src.schemas.users_schemas import UserRequestSchema, UserUpdateSchema
from src.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[UserModel, UserRequestSchema, UserUpdateSchema]):
    def get_by_id(self, db: Session, *, id: str) -> Optional[UserModel]:
        return super().get_by_id(db, id)

    def get_by_email(self, db: Session, *, email: str) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.email == email).first()
        
    def get_by_username(self, db: Session, *, username: str) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.username == username).first()

    def get_all(self, db: Session, *, skip: int, limit: int) -> List[UserModel]:
        return super().get_all(db, skip=skip, limit=limit)

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
        
    def is_admin(self, db: Session, *, id: str):
        user = self.get_by_id(db, id)
        if user.entity != "administrator":
            return False
        
        return True       

UserRepository = UserRepository(UserModel)