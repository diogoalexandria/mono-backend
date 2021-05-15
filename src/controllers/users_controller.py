from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.schemas.users_schemas import UserResponseSchema, UserRequestSchema
from src.database.session import db_session
from src.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create(*,db: Session = Depends(db_session), req_user: UserRequestSchema) -> Any:
    user = UserRepository.get_by_username(db, username=req_user.username)
    if user:
        raise HTTPException( status_code=400, detail="O username já está cadastrado." )
    user = UserRepository.get_by_email(db, email=req_user.email)
    if user:
        raise HTTPException( status_code=400, detail="O email já está cadastrado." )
    
    user = UserRepository.create(db, req_object=req_user)

    return user

@router.get('/users', response_model=List[UserResponseSchema])
def list_users(*,db: Session = Depends(db_session)) -> Any:
    pass

@router.get('/protected')
def protected(username=Depends(Auth.wrapper)):
    return {"name": username}