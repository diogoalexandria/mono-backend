from typing import Generic, TypeVar, Type, Any, Optional, List, Union, Dict
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from src.database.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
RequestSchemaType = TypeVar("RequestSchemaType", bound=BaseModel)
UpdateRequestSchemaType = TypeVar("UpdateRequestSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, RequestSchemaType, UpdateRequestSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model)\
                .filter(self.model.id == id)\
                .first()
    
    def get_all(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model)\
                 .offset(skip)\
                 .limit(limit)\
                 .all()

    def create(self, db: Session, *, req_object: RequestSchemaType) -> ModelType:
        json_object = jsonable_encoder(req_object)
        db_object = self.model(**json_object)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)

        return db_object

    def update(self, db:Session, *, db_object: ModelType, req_object: Union[UpdateRequestSchemaType, dict]):
        
        incoming_object = req_object.dict(exclude_unset=True)
        
        updated_object = db_object.copy(update=incoming_object)

        db.add(updated_object)
        db.commit()
        db.refresh(updated_object)

        # json_object = jsonable_encoder(db_object)

        # if isinstance(req_object, dict):
        #     update_object = req_object
        # else:
        #     update_object = req_object.dict(exclude_unset=True)
        
        # for field in json_object:
        #     if field in update_object:
        #         setattr(db_object, field, update_object[field])
        
        # db.add(db_object)
        # db.commit()
        # db.refresh(db_object)
        
        return db_object

    def remove(self, db: Session, *, id: int) -> ModelType:
        db_object = db.query(self.model).get(id)
        db.delete(db_object)
        db.commit()
        
        return db_object