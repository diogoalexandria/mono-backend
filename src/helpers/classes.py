from typing import Any, Union
from src.schemas.classes_schemas import ClassResponseSchema, ClassSchema

def response_class(class_item: Union[ClassSchema, Any]) -> ClassResponseSchema:    
    return ClassResponseSchema(
        id=class_item.id,
        name=class_item.name,
        subject_id=class_item.subject_id,
        professor_id=class_item.professor_id,
        status=class_item.status        
    )