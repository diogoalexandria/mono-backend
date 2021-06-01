from uuid import UUID
from typing import Union
from fastapi import HTTPException
from src.helpers.uuid import is_UUID
from src.helpers.email import is_email
from src.models.users_model import UsersModel
from sqlalchemy.orm.session import Session
from src.repositories.users_repository import UsersRepository

class UsersService():
    def get_user( self, db: Session, *,identity: Union[str, UUID] ) -> UsersModel:        
        if is_email(identity):
            user = UsersRepository.get_by_email( db, email=identity )
        elif is_UUID(identity):
            user = UsersRepository.get_by_id( db, id=identity )
        else:
            user = UsersRepository.get_by_username( db, username=identity )

        return user    

    def validate_email( self, db: Session, *, email: str ):
        if not is_email():
            raise HTTPException( status_code=400, detail="Email inválido" )

        email_exist = UsersRepository.get_by_email( db, email=email )
        if email_exist:
            raise HTTPException( status_code=400, detail="O email já está cadastrado." )
    
    def validate_username( self, db: Session, *, username: str ):
        username_exist = UsersRepository.get_by_username(db, username=username)
        if username_exist:
            raise HTTPException( status_code=400, detail="O username já está cadastrado." )

    def validate_id( self, db: Session, *, id: str = id ) -> UsersModel:
        user = UsersRepository.get_by_id( db, id=id )
        if not user:        
            raise HTTPException( status_code=400, detail="Usuário não encontrado." )

        return user

UsersService = UsersService()
