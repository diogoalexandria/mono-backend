from typing import Any, List, Union, Dict, Any
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from src.config import DATABASE_URL
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.helpers.users import is_admin, is_current_user, create_response_user
from src.database.session import db_session
from src.schemas.users_schemas import StatusOptions, UserResponseSchema, UserRequestSchema, ListUsersRequestSchema, UserUpdateSchema
from src.repositories.users_repository import UsersRepository
from src.services.users_service import UsersService

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_user: UserRequestSchema ) -> Any:        
    if not is_admin(db, id=income_id):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    UsersService.validate_username(db, username=new_user.username)
    UsersService.validate_email(db, email=new_user.email)    
    
    created_user = UsersRepository.create(db, req_object=new_user)
    
    return create_response_user(created_user)


@router.get('/users', response_model=List[UserResponseSchema])
def list_users( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session),  config: ListUsersRequestSchema ) -> Any:    
    skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
    users = UsersRepository.get_all(db, skip=skip, limit=limit)
    
    response_users = []
    for user in users:
        response_users.append(create_response_user(user))
    
    return response_users


@router.get('/users/{id}', response_model=UserResponseSchema)
def list_user( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:

    user = UsersService.validate_id(db, id=id)

    return create_response_user(user)


@router.patch('/users/{id}', response_model=UserResponseSchema, status_code=202)
def update(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[UserUpdateSchema,  Dict[str, Union[str, StatusOptions]]],
    id: str = id 
    
) -> Any:
    
    if not is_admin( db, id = income_id) and not is_current_user(income_id=income_id, action_id=id ):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    current_user = UsersService.validate_id(db, id=id)

    # Reforçando que o id que chega no Params seja o mesmo que o Request Body
    new_infos['id'] = id 
       
    if "email" in new_infos:
        UsersService.validate_email(db, email=new_infos.email)
    if "username" in new_infos:
        UsersService.validate_username(db, username=new_infos.username)    
    if "password" in new_infos:       
        new_infos["password"] = Auth.hash_password(new_infos["password"])

    updated_user = UsersRepository.update(db, db_object=current_user, req_object=new_infos)
    
    return create_response_user(updated_user)


@router.delete('/users/{id}', response_model=UserResponseSchema)
def remove( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    if not is_admin(db, id=income_id):
        raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )
    
    removed_user = UsersRepository.remove(db, id=id)

    return create_response_user(removed_user)
