from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.helpers.auth import verify_password
from src.helpers.user import is_active
from src.helpers.email import is_email
from src.database.session import db_session
from src.schemas.auth_schema import AuthRequestSchema
from src.repositories.user_repository import get_by_email, get_by_username

router = APIRouter()

@router.post('/auth', response_model=UserResponseSchema)
def login(payload: AuthRequestSchema, db: Session = Depends(db_session)) -> Any:
    identity, password = payload.values()

    if is_email(identity):
        user = get_by_email(db, email=identity)
    else:
        user = get_by_username(db, username=identity)
    
    if not user:
        raise HTTPException(status_code=400, detail="Usuário inexistente.")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Senha incorreta.")
    if not is_active(user):
        raise HTTPException(status_code=400, detail="Usuário desativado.")
    