from typing import Optional
from base_repository import BaseRepository
from helpers.security import Auth
from src.models.user_model import UserModel
from src.schema.users_schemas import UserRequestSchema, UserUpdateSchema

class UserRepository(BaseRepository[UserModel, UserRequestSchema, UserUpdateSchema]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.email == email).first()
        
    def get_by_username(self, db: Session, *, username: str):
        return db.query(UserModel).filter(UserModel.username == username).first()

    def create(self, db: Session, *, req_object: UserRequestSchema) -> User:
        db_object = UserModel(
            email=req_object.email    
        )
        pass


UserRepository = UserRepository(UserModel)