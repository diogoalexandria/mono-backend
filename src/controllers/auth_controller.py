from typing import Any
from fastapi import APIRouter, Depends
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.schemas.auth_schemas import AuthRequestSchema, AuthSchema
from src.services.auth_service import AuthService
from src.services.users_service import UsersService

router = APIRouter()

@router.post( '/auth', response_model=AuthSchema )
def login( payload: AuthRequestSchema, *, db: Session = Depends(db_session) ) -> Any:    
    identity, password = dict(payload).values() # Desestruturando (Unpacking) os valores do Request Body payload    
    
    user = UsersService.get_user( db, identity=identity )           
    AuthService.validate_access( user, password )
    token = AuthService.get_token( user.id )    
    # refresh_token = AuthService.get_refresh_token( user.id )   

    return {
        'token': token,
        'entity': user.entity        
    }
