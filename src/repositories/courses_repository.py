from typing import Any, Dict, List, Optional
from sqlalchemy.orm.session import Session
from src.schemas.courses_schema import CourseBaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.courses_model import CoursesModel

class CoursesRepository( BaseRepository[CoursesModel, CourseBaseSchema, CourseBaseSchema] ):
    def create(self, db: Session, *, req_object: CourseBaseSchema) -> CoursesModel:
        return super().create(db, req_object)

    def get_by_id(self, db: Session, id: str) -> Optional[CoursesModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[CoursesModel]:
        return db.query( CoursesModel ).filter( CoursesModel.name == name ).first()
    
    def get_all(self, db: Session, *, skip: int, limit: int) -> List[CoursesModel]:
        return super().get_all(db, skip=skip, limit=limit)

    def update(self, db: Session, *, db_object:CoursesModel, req_object: Union[CourseBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object, req_object)

    def remove(self, db: Session, *, id: str) -> CoursesModel:
        return super().remove(db, id)

CoursesRepository = CoursesRepository( CoursesModel )