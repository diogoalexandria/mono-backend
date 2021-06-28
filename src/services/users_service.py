from uuid import UUID
from typing import Dict, Union
from fastapi import HTTPException
from src.helpers.auth import Auth
from src.helpers.uuid import is_UUID
from src.helpers.email import is_email
from src.helpers.users import response_user
from src.models.users_model import UsersModel
from sqlalchemy.orm.session import Session
from src.schemas.users_schemas import StatusOptions, UserRequestSchema, UserResponseSchema, UserUpdateSchema
from src.repositories.users_repository import UsersRepository

class UsersService():
    def get_user( self, db: Session, *, identity: Union[str, UUID] ) -> UsersModel:        
        if is_email(identity):
            user = UsersRepository.get_by_email( db, email=identity )
        elif is_UUID(identity):
            user = UsersRepository.get_by_id( db, id=identity )
        else:
            user = UsersRepository.get_by_username( db, username=identity )           

        return user   


    def validate_email( self, db: Session, *, email: str ):
        if not is_email(email):
            raise HTTPException( status_code=400, detail="Email inválido" )

        email_exist = UsersRepository.get_by_email( db, email=email )
        if email_exist:
            raise HTTPException( status_code=400, detail="O email já está cadastrado." )

    
    def validate_username( self, db: Session, *, username: str ):
        username_exist = UsersRepository.get_by_username(db, username=username)
        if username_exist:
            raise HTTPException( status_code=400, detail="O username já está cadastrado." )


    def validate_id( self, db: Session, *, id: str = id ) -> Dict[UsersModel,UserResponseSchema]:
        user = UsersRepository.get_by_id( db, id=id )        
        if not user:        
            raise HTTPException( status_code=400, detail="Usuário não encontrado." )

        return {
            "db_object": user,
            "response": response_user(user)
        }


    def create_user( self, db: Session, *, object: UserRequestSchema ):
        created_user = UsersRepository.create(db, req_object=object)
    
        return response_user(created_user)


    def create_users_list( self, db: Session, ):
         # Desestruturando (Unpacking) os valores do Request Body config
        users = UsersRepository.get_all(db)
                
        response_users = [response_user(user) for user in users]        
        
        return response_users

    
    def create_users_topic_list( self, db: Session, *, id: str = id ):
         # Desestruturando (Unpacking) os valores do Request Body config          
        users = UsersRepository.get_by_topic(db, id=id)
                
        response_users = [response_user(user) for user in users]        
        
        return response_users


    def update_user(

        self,
        db: Session,
        *,
        db_object: UsersModel,
        infos_object: Union[UserUpdateSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        # infos_object['id'] = id 
        
        if "email" in infos_object:
            UsersService.validate_email(db, email=infos_object.email)
        if "username" in infos_object:
            UsersService.validate_username(db, username=infos_object.username)    
        if "password" in infos_object:       
            infos_object["password"] = Auth.hash_password(infos_object["password"])

        updated_user = UsersRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_user(updated_user)


    def remove_user( self, db: Session, *, id: str = id ):        
        removed_user = UsersRepository.remove(db, id=id)

        return response_user(removed_user)
        

UsersService = UsersService()
