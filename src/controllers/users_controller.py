from fastapi import APIRouter
from src.models.user_model import UserModel
from src.schema.users_schemas import UserResponseSchema
from src.repositories.user_repository import User

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create(user: UserModel) -> Any:
    new_user = User
    