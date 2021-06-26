from datetime import datetime
from src.models.users_model import UsersModel
from src.schemas.subscriptions_schemas import SubscriptionBaseSchema
from src.models.subscriptions_model import SubscriptionsModel
import uuid
from src.schemas.status_schema import StatusOptions
from typing import Any, Dict, List, Optional, Union
from sqlalchemy.orm.session import Session
from src.repositories.base_repository import BaseRepository

class SubscriptionsRepository( BaseRepository[SubscriptionsModel, SubscriptionBaseSchema, SubscriptionBaseSchema] ):
    def create(self, db: Session, *, req_object: SubscriptionBaseSchema) -> SubscriptionsModel:
        db_object = SubscriptionsModel(

            id=uuid.uuid4(),
            sub_date=datetime.utcnow(),    
            class_id=req_object.class_id,
            student_id=req_object.student_id,            
            status=StatusOptions.active,
            created_at=datetime.utcnow()

        )
        return super().create(db, req_object=db_object)

    def get_by_id(self, db: Session, id: str) -> Optional[SubscriptionsModel]:
        return super().get_by_id(db, id)
    
    def get_by_name(self, db: Session, name: str) -> Optional[SubscriptionsModel]:
        return db.query( SubscriptionsModel ).filter( SubscriptionsModel.name == name ).first()
    
    def get_by_class_id(self, db: Session, id: str) -> List[Any]:        
        return db.query(self.model, UsersModel)\
                .join(UsersModel)\
                .filter(self.model.student_id == UsersModel.id)\
                .filter(self.model.class_id == id)\
                .filter(UsersModel.status == "active")\
                .all()
    
    def get_all(self, db: Session) -> List[SubscriptionsModel]:
        return super().get_all(db)

    def update(self, db: Session, *, db_object:SubscriptionsModel, req_object: Union[SubscriptionBaseSchema, Dict[str, Any]]):
        return super().update(db, db_object=db_object, req_object=req_object)

    def remove(self, db: Session, *, id: str) -> SubscriptionsModel:                       
        return super().remove(db, id=id)

SubscriptionsRepository = SubscriptionsRepository( SubscriptionsModel )