from typing import Any, List
from sqlalchemy.sql.functions import user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.schemas.users_schemas import UserResponseSchema, UserRequestSchema, ListUsersRequestSchema
from src.database.session import db_session
from src.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create(user_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_user: UserRequestSchema) -> Any:
    
    if not UserRepository.is_admin(db, id=user_id):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    user_exist = UserRepository.get_by_username(db, username=new_user.username)
    if user_exist:
        raise HTTPException( status_code=400, detail="O username já está cadastrado." )

    user_exist = UserRepository.get_by_email(db, email=new_user.email)
    if user_exist:
        raise HTTPException( status_code=400, detail="O email já está cadastrado." )
    
    created_user = UserRepository.create(db, req_object=new_user)

    response_user = UserResponseSchema(
        id=created_user.id,
        email=created_user.email,
        username=created_user.username,
        first_name=created_user.first_name,
        last_name=created_user.last_name    
    )

    return response_user

@router.get('/users', response_model=List[UserResponseSchema])
def list_users(*, db: Session = Depends(db_session),  config: ListUsersRequestSchema) -> Any:
    skip, limit = dict(config).values()    
    users = UserRepository.get_all(db, skip=skip, limit=limit)
    response_users = []
    for user in users:
        response_users.append(
            UserResponseSchema(
                id = user.id,
                email=user.email,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name 
            )
        )
    
    return response_users



@router.get('/protected')
def protected(user_id=Depends(Auth.wrapper)):
    return {"user_id": user_id}