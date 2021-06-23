from datetime import datetime
import uuid
from src.schemas.status_schema import StatusOptions
from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm.session import Session
from src.schemas.courses_schemas import CourseBaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.courses_model import CoursesModel

class CoursesRepository( BaseRepository[CoursesModel, CourseBaseSchema, CourseBaseSchema] ):
    def create(self, db: Session, *, req_object: CourseBaseSchema) -> CoursesModel:
        db_object = CoursesModel(

            id=uuid.uuid4(),            
            name=req_object.name,            
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )
        return super().create(db, req_object=db_object)

    def get_by_id(self, db: Session, id: str) -> Optional[CoursesModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[CoursesModel]:
        return db.query( CoursesModel ).filter( CoursesModel.name == name ).first()
    
    def get_all(self, db: Session) -> List[CoursesModel]:
        return super().get_all(db)

    def update(self, db: Session, *, db_object:CoursesModel, req_object: Union[CourseBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object=db_object, req_object=req_object)

    def remove(self, db: Session, *, id: str) -> CoursesModel:
        id = str(id)
        return super().remove(db, id=id)

CoursesRepository = CoursesRepository( CoursesModel )