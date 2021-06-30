import uuid
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from src.models.users_model import UsersModel
from src.repositories.base_repository import BaseRepository
from src.schemas.attendances_schemas import AttendanceBaseSchema, AttendancesListSchema
from src.models.attendances_model import AttendancesModel
from src.models.subscriptions_model import SubscriptionsModel
from src.models.classes_model import ClassesModel
from src.models.topics_model import TopicsModel
from src.schemas.status_schema import StatusOptions
from sqlalchemy.orm.session import Session

class AttendancesRepository( BaseRepository[AttendancesModel, AttendanceBaseSchema, AttendanceBaseSchema] ):
    def create(self, db: Session, *, req_object: AttendanceBaseSchema) -> AttendancesModel:
        db_object = AttendancesModel(

            id=uuid.uuid4(),
            topic_id=req_object.topic_id,             
            student_id=req_object.student_id,    
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )
        return super().create(db, req_object=db_object)

    def validate(self, db: Session, *, attendance: AttendanceBaseSchema) -> AttendanceBaseSchema:
        item = db.query(ClassesModel)\
                 .join(SubscriptionsModel)\
                 .join(TopicsModel)\
                 .filter(SubscriptionsModel.student_id == attendance.student_id)\
                 .filter(TopicsModel.id == attendance.topic_id)\
                 .all()
        if item:
            return { 
                "student_id": attendance.student_id,
                "topic_id": attendance.topic_id
            }
        else: 
            return
    
    def create_multi(self, db: Session, attendances: AttendancesListSchema) -> List[AttendancesModel]:
        list_objects = [AttendancesModel(

            id=uuid.uuid4(),
            topic_id=attendance["topic_id"],             
            student_id=attendance["student_id"],            
            created_at=datetime.utcnow()

        )for attendance in attendances]

        db_objects = [self.model(**jsonable_encoder(req_object)) for req_object in list_objects]
        db.bulk_save_objects(db_objects)        
        db.commit()
        # db.refresh(db_objects)

        return db_objects            
        

    def get_by_id(self, db: Session, id: str) -> Optional[AttendancesModel]:
        return super().get_by_id(db, id)

    def get_by_topic(self, db: Session, id: str) -> List[Any]:        
        return db.query(self.model,UsersModel)\
                 .join(UsersModel)\
                 .filter(self.model.topic_id == id)\
                 .all() 
    
    def get_by_name(self, db: Session, name: str) -> Optional[AttendancesModel]:
        return db.query( AttendancesModel ).filter( AttendancesModel.name == name ).first()
    
    def get_all(self, db: Session) -> List[AttendancesModel]:
        return super().get_all(db)

    def update(self, db: Session, *, db_object:AttendancesModel, req_object: Union[AttendanceBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object=db_object, req_object=req_object)

    def remove(self, db: Session, *, id: str) -> AttendancesModel:                       
        return super().remove(db, id=id)

AttendancesRepository = AttendancesRepository( AttendancesModel )