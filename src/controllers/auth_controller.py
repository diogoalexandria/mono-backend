from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.helpers.user import is_active
from src.helpers.email import is_email
from src.database.session import db_session
from src.schemas.auth_schemas import AuthRequestSchema
from src.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/auth')
def login(payload: AuthRequestSchema, db: Session = Depends(db_session)) -> Any:
    identity, password = payload.values()

    if is_email(identity):
        user = UserRepository.get_by_email(db, email=identity)
    else:
        user = UserRepository.get_by_username(db, username=identity)
    
    if not user:
        raise HTTPException(status_code=400, detail="Usuário inexistente.")
    if not Auth.verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Senha incorreta.")
    if not is_active(user):
        raise HTTPException(status_code=400, detail="Usuário desativado.")
    
    token = Auth.encode_token(user.id)
    
    return {
        'token': token
    }