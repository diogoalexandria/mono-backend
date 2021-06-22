import uuid
from typing import Optional, List, Union, Dict, Any
from datetime import datetime
from sqlalchemy.orm import Session 
from src.helpers.auth import Auth
from src.models.users_model import UsersModel
from src.schemas.users_schemas import UserRequestSchema, UserUpdateSchema, StatusOptions
from src.repositories.base_repository import BaseRepository

class UsersRepository( BaseRepository[UsersModel, UserRequestSchema, UserUpdateSchema] ):
    def create( self, db: Session, *, req_object: UserRequestSchema ) -> UsersModel:
        db_object = UsersModel(

            id=uuid.uuid4(),
            email=req_object.email,
            username=req_object.username,
            first_name=req_object.first_name,
            last_name=req_object.last_name,
            entity=req_object.entity,
            gender=req_object.gender,
            password=Auth.hash_password(req_object.password),
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )

        db.add( db_object )
        db.commit()
        db.refresh( db_object )

        return db_object

    def get_by_email( self, db: Session, *, email: str ) -> Optional[UsersModel]:
        return db.query( UsersModel ).filter( UsersModel.email == email ).first()
        
    def get_by_username( self, db: Session, *, username: str ) -> Optional[UsersModel]:        
        return db.query( UsersModel ).filter( UsersModel.username == username ).first()

    def get_by_id( self, db: Session, *, id: str) -> Optional[UsersModel]:
        return super().get_by_id(db, id=id)

    def get_all( self, db: Session ) -> List[UsersModel]:
        return super().get_all( db )

    def update( self, db: Session, *, db_object: UsersModel, req_object: Union[UserUpdateSchema,  Dict[str, Any]] ):
        return super().update( db, db_object=db_object, req_object=req_object )

    def remove( self, db: Session, *, id: str ) -> UsersModel:
        return super().remove( db, id=id )       
          
UsersRepository = UsersRepository( UsersModel )