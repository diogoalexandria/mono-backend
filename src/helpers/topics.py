from os import name
from src.schemas.topics_schemas import TopicProfessorResponseSchema, TopicResponseSchema, TopicSchema
from src.schemas.subscriptions_schemas import SubscriptionResponseSchema, SubscriptionSchema
from typing import Any, Union


def response_topic(topic: Union[TopicSchema, Any]) -> TopicResponseSchema:       
    return TopicResponseSchema(
        id=topic.id,                
        class_id=topic.class_id,
        topic_date=str(topic.topic_date),            
        status=topic.status        
    )

def response_topic_professor(result: Union[TopicSchema, Any]) -> TopicProfessorResponseSchema:
    topic, class_item = result       
    return TopicProfessorResponseSchema(
        id=topic.id,
        name=class_item.name,                
        subject_id=class_item.subject_id,        
        topic_date=str(topic.topic_date),            
        status=topic.status        
    )
