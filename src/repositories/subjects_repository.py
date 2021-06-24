from datetime import datetime
import uuid
from src.schemas.status_schema import StatusOptions
from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm.session import Session
from src.models.subjects_model import SubjectsModel
from src.schemas.subjects_schemas import SubjectBaseSchema
from src.repositories.base_repository import BaseRepository

class SubjectsRepository( BaseRepository[SubjectsModel, SubjectBaseSchema, SubjectBaseSchema] ):
    def create(self, db: Session, *, req_object: SubjectBaseSchema) -> SubjectsModel:
        db_object = SubjectsModel(

            id=uuid.uuid4(),            
            name=req_object.name,            
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )
        return super().create(db, req_object=db_object)

    def get_by_id(self, db: Session, id: str) -> Optional[SubjectsModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[SubjectsModel]:
        return db.query( SubjectsModel ).filter( SubjectsModel.name == name ).first()
    
    def get_all(self, db: Session) -> List[SubjectsModel]:
        return super().get_all(db)

    def update(self, db: Session, *, db_object:SubjectsModel, req_object: Union[SubjectBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object=db_object, req_object=req_object)

    def remove(self, db: Session, *, id: str) -> SubjectsModel:
        id = str(id)
        return super().remove(db, id=id)

SubjectsRepository = SubjectsRepository( SubjectsModel )