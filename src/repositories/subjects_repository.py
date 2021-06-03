from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm.session import Session
from src.models.subjects_model import SubjectsModel
from src.schemas.subjects_schemas import SubjectBaseSchema
from src.repositories.base_repository import BaseRepository

class SubjectsRepository( BaseRepository[SubjectsModel, SubjectBaseSchema, SubjectBaseSchema] ):
    def create(self, db: Session, *, req_object: SubjectBaseSchema) -> SubjectsModel:
        return super().create(db, req_object)

    def get_by_id(self, db: Session, id: str) -> Optional[SubjectsModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[SubjectsModel]:
        return db.query( SubjectsModel ).filter( SubjectsModel.name == name ).first()
    
    def get_all(self, db: Session, *, skip: int, limit: int) -> List[SubjectsModel]:
        return super().get_all(db, skip=skip, limit=limit)

    def update(self, db: Session, *, db_object:SubjectsModel, req_object: Union[SubjectBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object, req_object)

    def remove(self, db: Session, *, id: str) -> SubjectsModel:
        return super().remove(db, id)

SubjectsRepository = SubjectsRepository( SubjectsModel )