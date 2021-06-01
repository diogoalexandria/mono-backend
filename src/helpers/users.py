from uuid import UUID
from typing import Union, Any
from sqlalchemy.orm.session import Session
from src.models.users_model import UsersModel
from src.repositories.users_repository import UsersRepository
from src.schemas.users_schemas import UsersEntities, StatusOptions, UserResponseSchema, UserSchema

def is_active(user: UsersModel) -> bool:
    return user.status == StatusOptions.active

def is_admin(db: Session, *, id: str) -> bool:
    user = UsersRepository.get_by_id(db, id=id)    
    return user.entity == UsersEntities.administrator

def is_current_user(income_id: str, action_id: UUID) -> bool:
    return income_id == str(action_id)

def create_response_user(user: Union[UserSchema, Any]) -> UserResponseSchema:    
    return UserResponseSchema(
        id=user.id,
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name
    )