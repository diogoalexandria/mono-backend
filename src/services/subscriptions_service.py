from src.models.subscriptions_model import SubscriptionsModel
from src.repositories.subscriptions_repository import SubscriptionsRepository
from src.helpers.subscriptions import response_subscription, response_subscription_user
from src.schemas.subscriptions_schemas import SubscriptionBaseSchema
from src.schemas.status_schema import StatusOptions
from typing import Dict, Union
from fastapi import HTTPException

from sqlalchemy.orm.session import Session


class SubscriptionsService():
    def create_subscription( self, db: Session, *, object: SubscriptionBaseSchema ):
       subscription = SubscriptionsRepository.create(db, req_object=object)

       return response_subscription(subscription)


    def create_subscriptions_list( self, db: Session ):        
        # skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        subscriptions = SubscriptionsRepository.get_all(db)
        
        response_subscriptions = [response_subscription(subscription) for subscription in subscriptions]
        
        return response_subscriptions
    
    def create_subscriptions_users_list(self, db: Session, id: str):        
        subscriptions_users = SubscriptionsRepository.get_by_class_id(db, id=id)
        print(subscriptions_users)
        
        response_subscriptions_users = [response_subscription_user(subscription) for subscription in subscriptions_users]
        
        return response_subscriptions_users

    def validate_name( self, db: Session, *, name: str ):
        name_exist = SubscriptionsRepository.get_by_name(db, name=name)
        if name_exist:
            raise HTTPException( status_code=400, detail="O nome já está cadastrado." )


    def validate_id( self, db: Session, *, id: str = id ) -> SubscriptionsModel:
        subscription = SubscriptionsRepository.get_by_id( db, id=id )
        if not subscription:        
            raise HTTPException( status_code=400, detail="Inscrição não encontrado." )
        
        return {
            "db_object": subscription,
            "response": response_subscription(subscription)
        }


    def update_subscription(

        self,
        db: Session,
        *,
        db_object: SubscriptionsModel,
        infos_object: Union[SubscriptionBaseSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        # infos_object['id'] = id        

        updated_subscription = SubscriptionsRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_subscription(updated_subscription)

    def remove_subscription( self, db: Session, *, id: str = id ):               
        removed_subscription = SubscriptionsRepository.remove(db, id=id)

        return response_subscription(removed_subscription)


SubscriptionsService = SubscriptionsService()