from typing import Any, List
from sqlalchemy.sql.functions import user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.schemas.users_schemas import UserResponseSchema, UserRequestSchema
from src.database.session import db_session
from src.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create(user_id=Depends(Auth.wrapper),*,db: Session = Depends(db_session), new_user: UserRequestSchema) -> Any:
    
    if not UserRepository.is_admin(db, id=user_id, repository=UserRepository):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    user_exist = UserRepository.get_by_username(db, username=new_user.username)
    if user_exist:
        raise HTTPException( status_code=400, detail="O username já está cadastrado." )

    user_exist = UserRepository.get_by_email(db, email=new_user.email)
    if user_exist:
        raise HTTPException( status_code=400, detail="O email já está cadastrado." )
    
    created_user = UserRepository.create(db, req_object=new_user)

    return created_user

@router.get('/users', response_model=List[UserResponseSchema])
def list_users(req_user_id=Depends(Auth.wrapper),*,db: Session = Depends(db_session)) -> Any:
    req_user = UserRepository.get_by_id(db, id=req_user_id)
    print(req_user.entity)
    print(type(req_user.entity))
    pass

@router.get('/protected')
def protected(user_id=Depends(Auth.wrapper)):
    return {"user_id": username}