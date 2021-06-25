from datetime import datetime
import uuid
from src.schemas.status_schema import StatusOptions
from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm.session import Session
from src.schemas.classes_schemas import ClassBaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.classes_model import ClassesModel

class ClassesRepository( BaseRepository[ClassesModel, ClassBaseSchema, ClassBaseSchema] ):
    def create(self, db: Session, *, req_object: ClassBaseSchema) -> ClassesModel:
        db_object = ClassesModel(

            id=uuid.uuid4(),            
            name=req_object.name,
            subject_id=req_object.subject_id,
            professor_id=req_object.professor_id,            
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )
        return super().create(db, req_object=db_object)

    def get_by_id(self, db: Session, id: str) -> Optional[ClassesModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[ClassesModel]:
        return db.query( ClassesModel ).filter( ClassesModel.name == name ).first()
    
    def get_all(self, db: Session) -> List[ClassesModel]:
        return super().get_all(db)

    def update(self, db: Session, *, db_object:ClassesModel, req_object: Union[ClassBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object=db_object, req_object=req_object)

    def remove(self, db: Session, *, id: str) -> ClassesModel:
        print(f'3: {id}')
        print(type(id))               
        return super().remove(db, id=id)

ClassesRepository = ClassesRepository( ClassesModel )
