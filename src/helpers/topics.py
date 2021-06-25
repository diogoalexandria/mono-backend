from src.schemas.topics_schemas import TopicResponseSchema, TopicSchema
from src.schemas.subscriptions_schemas import SubscriptionResponseSchema, SubscriptionSchema
from typing import Any, Union


def response_topic(topic: Union[TopicSchema, Any]) -> TopicResponseSchema:    
    return TopicResponseSchema(
        id=topic.id,        
        class_id=topic.class_id,
        student_id=topic.student_id,
        created_at=str(topic.created_at),
        status=topic.status        
    )