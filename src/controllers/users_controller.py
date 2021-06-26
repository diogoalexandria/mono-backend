from src.models.users_model import UsersModel
from typing import Any, List, Union, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.helpers.auth import Auth
from src.database.session import db_session
from src.schemas.users_schemas import StatusOptions, UserResponseSchema, UserRequestSchema, UserUpdateSchema
from src.services.auth_service import AuthService
from src.services.users_service import UsersService

router = APIRouter()

@router.post('/users', response_model=UserResponseSchema, status_code=201)
def create_user(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_user: UserRequestSchema) -> Any:
    AuthService.validate_admin_access(db, id=income_id)

    UsersService.validate_username(db, username=new_user.username)
    UsersService.validate_email(db, email=new_user.email)

    created_user = UsersService.create_user(db, object=new_user)

    return created_user


@router.get('/users', response_model=List[UserResponseSchema])
def list_users(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session)) -> Any:    
    users_list = UsersService.create_users_list(db)    
    return users_list 


@router.get('/users/{id}', response_model=UserResponseSchema)
def list_user(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id) -> Any:
    user = UsersService.validate_id(db, id=id)

    return user["response"]


@router.patch('/users/{id}', response_model=UserResponseSchema, status_code=202)
def update_user(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[UserUpdateSchema,  Dict[str, Union[str, StatusOptions]]],
    id: str = id

) -> Any:
    AuthService.validate_admin_or_current_access(
        db,
        income_id=income_id,
        action_id=id
    )

    current_user = UsersService.validate_id(db, id=id)    
    updated_user = UsersService.update_user(
        db,
        db_object=current_user["db_object"],
        infos_object=new_infos
    )

    return updated_user


@router.delete('/users/{id}', response_model=UserResponseSchema)
def remove_user(income_id=Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id):
    AuthService.validate_admin_access(db, id=income_id)    
    removed_user = UsersService.remove_user(db, id=id)
    return removed_user
