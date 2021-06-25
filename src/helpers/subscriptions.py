from src.schemas.subscriptions_schemas import SubscriptionResponseSchema, SubscriptionSchema
from typing import Any, Union


def response_subscription(subscription: Union[SubscriptionSchema, Any]) -> SubscriptionResponseSchema:    
    return SubscriptionResponseSchema(
        id=subscription.id,        
        class_id=subscription.class_id,
        student_id=subscription.student_id,
        created_at=str(subscription.created_at),
        status=subscription.status        
    )