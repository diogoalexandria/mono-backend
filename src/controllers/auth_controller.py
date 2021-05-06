from fastapi import APIRouter
from src.schemas.auth_schema import AuthRequestSchema

router = APIRouter()

@router.post('/auth', response_model=UserResponseSchema)
def login(payload: AuthRequestSchema) -> Any:
    new_user = User