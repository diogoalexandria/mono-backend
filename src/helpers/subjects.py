from typing import Any, Union
from src.schemas.subjects_schemas import SubjectBaseSchema, SubjectSchema

def response_subject(course: Union[SubjectSchema, Any]) -> SubjectBaseSchema:    
    return SubjectBaseSchema(
        name=course.name        
    )