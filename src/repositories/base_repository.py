from typing import Generic, TypeVar, Type, Optional, List, Union, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

ModelType = TypeVar("ModelType", bound=BaseModel)
RequestSchemaType = TypeVar("RequestSchemaType", bound=BaseModel)
UpdateRequestSchemaType = TypeVar("UpdateRequestSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, RequestSchemaType, UpdateRequestSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, id: str) -> Optional[ModelType]:
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

    def update(self, db:Session, *, db_object: ModelType, req_object: Union[UpdateRequestSchemaType, Dict[str, Any]]):
        json_object = jsonable_encoder(db_object)                  # Transformando o objeto do banco em um objeto iterável 
        
        if isinstance(req_object, dict):                                       # Teste se o objeto vindo da requisição é do tipo dict
            incoming_object = req_object
        else:                        
            incoming_object = req_object.dict(exclude_unset=True)        
        
        for field in json_object:
            if field == "id":
                continue                                  # Para cada campo no objeto iterável
            if field in incoming_object:                           # Se o campo também existe no objeto vindo com a novas infos
                setattr(db_object, field, incoming_object[field])  # Atualiza o objeto do banco com o valor do objeto da requisição
            if field == "updated_at":
                setattr(db_object, field, datetime.utcnow())
                
        db.add(db_object)
        db.commit()
        db.refresh(db_object)       
        
        return db_object

    def remove(self, db: Session, *, id: str) -> ModelType:        
        db_object = db.query(self.model).get(id)
        db.delete(db_object)
        db.commit()
        
        return db_object