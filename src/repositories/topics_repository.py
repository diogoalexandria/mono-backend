from datetime import datetime
from src.schemas.topics_schemas import TopicBaseSchema
from src.models.topics_model import TopicsModel
from src.schemas.subscriptions_schemas import SubscriptionBaseSchema
from src.models.subscriptions_model import SubscriptionsModel
import uuid
from src.schemas.status_schema import StatusOptions
from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm.session import Session
from src.repositories.base_repository import BaseRepository

class TopicsRepository( BaseRepository[TopicsModel, TopicBaseSchema, TopicBaseSchema] ):
    def create(self, db: Session, *, req_object: TopicBaseSchema) -> TopicsModel:
        db_object = TopicsModel(

            id=uuid.uuid4(),
            sub_date=datetime.utcnow(),    
            class_id=req_object.class_id,
            student_id=req_object.student_id,            
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )
        return super().create(db, req_object=db_object)

    def get_by_id(self, db: Session, id: str) -> Optional[TopicsModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[TopicsModel]:
        return db.query( TopicsModel ).filter( TopicsModel.name == name ).first()
    
    def get_all(self, db: Session) -> List[TopicsModel]:
        return super().get_all(db)

    def update(self, db: Session, *, db_object:TopicsModel, req_object: Union[TopicBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object=db_object, req_object=req_object)

    def remove(self, db: Session, *, id: str) -> TopicsModel:                       
        return super().remove(db, id=id)

TopicsRepository = TopicsRepository( TopicsModel )