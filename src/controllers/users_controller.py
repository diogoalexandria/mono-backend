from typing import Any, List, Union, Dict, Any
from fastapi import APIRouter, Depends, HTTPException
from src.config import DATABASE_URL
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.helpers.user import is_admin, is_current_user, create_response_user
from src.database.session import db_session
from src.schemas.users_schemas import UserResponseSchema, UserRequestSchema, ListUsersRequestSchema, UserUpdateSchema
from src.repositories.user_repository import UserRepository

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_user: UserRequestSchema) -> Any:        
    if not is_admin(db, id=income_id):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    user_exist = UserRepository.get_by_username(db, username=new_user.username)
    if user_exist:
        raise HTTPException( status_code=400, detail="O username já está cadastrado." )

    user_exist = UserRepository.get_by_email(db, email=new_user.email)
    if user_exist:
        raise HTTPException( status_code=400, detail="O email já está cadastrado." )
    
    created_user = UserRepository.create(db, req_object=new_user)
    
    return create_response_user(created_user)


@router.get('/users', response_model=List[UserResponseSchema])
def list_users(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session),  config: ListUsersRequestSchema) -> Any:    
    skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
    users = UserRepository.get_all(db, skip=skip, limit=limit)
    
    response_users = []
    for user in users:
        response_users.append(create_response_user(user))
    
    return response_users


@router.get('/users/{id}', response_model=UserResponseSchema)
def list_user(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), id=id) -> Any:       
    user = UserRepository.get_by_id(db, id=id)

    if not user:        
        raise HTTPException( status_code=400, detail="Usuário não encontrado." )  
    
    return create_response_user(user)


@router.patch('/users/{id}', response_model=UserResponseSchema, status_code=202)
def update(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[UserUpdateSchema,  Dict[str, Any]],
    id=id 
    
) -> Any:
    # Reforçando que o id que chega no Params seja o mesmo que o Request Body
    new_infos['id'] = id    
    
    if not is_admin(db, id=income_id) and not is_current_user(income_id=income_id, action_id=id):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    current_user = UserRepository.get_by_id(db, id=id)
    if not current_user:
        raise HTTPException( status_code=400, detail="Usuário não encontrado." )
    
    if "password" in new_infos:       
        new_infos["password"] = Auth.hash_password(new_infos["password"])

    updated_user = UserRepository.update(db, db_object=current_user, req_object=new_infos)
    
    return create_response_user(updated_user)


@router.delete('/users/{id}', response_model=UserResponseSchema)
def remove(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), id=id):
    if not is_admin(db, id=income_id):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )
    
    removed_user = UserRepository.remove(db, id=id)

    return create_response_user(removed_user)
