from sqlalchemy.orm.session import Session
from src.models.users_model import UsersModel
from typing import Union
from uuid import UUID
from fastapi import HTTPException
from src.helpers.auth import Auth
from src.helpers.users import is_active, is_admin, is_current_user, is_professor

class AuthService():
    def validate_access( self, user: Union[UsersModel, None], password: str ):
        if not user:
            raise HTTPException( status_code=400, detail="Usuário inexistente." )
        if not Auth.verify_password(password, user.password):
            raise HTTPException( status_code=400, detail="Senha incorreta." )
        if not is_active(user):
            raise HTTPException( status_code=400, detail="Usuário desativado." )

    def get_token( self, payload: Union[UUID, str] ):
        return Auth.encode_token( payload )
    
    def validate_token( self, token: str ):
        return Auth.decode_token( token )    

    def validate_admin_access( self, db: Session, *, id: str ):
        if not is_admin(db, id=id):
            raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )
    
    def validate_professor_access( self, db: Session, *, id: str ):
        if not is_professor(db, id=id):
            raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )

    def validate_admin_or_current_access( self, db: Session, *, income_id: str, action_id: str ):
        if not is_admin( db, id = income_id) and not is_current_user(income_id=income_id, action_id=action_id ):
            raise HTTPException( status_code=401, detail="Sem permissão para realizar essa ação." )
        

AuthService = AuthService()
