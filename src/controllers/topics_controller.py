from src.schemas.topics_schemas import TopicBaseSchema, TopicResponseSchema
from typing import Any
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.services.auth_service import AuthService

router = APIRouter()


@router.post('/topics', response_model=TopicResponseSchema, status_code=201)
def create_topic( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_topic: TopicBaseSchema ) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    # ClassesService.validate_name(db, name=new_class.name)

    created_topic = SubscriptionsService.create_subscription(db, object=new_topic)
    
    return created_topic

@router.get('/subscriptions', response_model=List[SubscriptionResponseSchema])
def list_subscriptions( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    subscriptions_list = SubscriptionsService.create_subscriptions_list(db)

    return subscriptions_list


@router.get('/subscriptions/{id}', response_model=SubscriptionResponseSchema)
def list_subscription( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    subscription = SubscriptionsService.validate_id(db, id=id)
    
    return subscription["response"]
    

@router.patch('/subscriptions/{id}', response_model=SubscriptionResponseSchema, status_code=202)
def update_subscription(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[SubscriptionBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_subscription = SubscriptionsService.validate_id(db, id=id)
    updated_subscription = SubscriptionsService.update_subscription(
        db,
        db_object=current_subscription["db_object"],
        infos_object=new_infos
    )
    
    return updated_subscription


@router.delete('/subscriptions/{id}', response_model=SubscriptionResponseSchema)
def remove_subscription( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)
       
    removed_subscription = SubscriptionsService.remove_subscription(db, id=id)

    return removed_subscription