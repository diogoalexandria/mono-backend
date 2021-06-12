from typing import Any, Union
from src.schemas.subjects_schemas import SubjectResponseSchema, SubjectSchema

def response_subject(subject: Union[SubjectSchema, Any]) -> SubjectResponseSchema:    
    return SubjectResponseSchema(
        id=subject.id,
        name=subject.name        
    )