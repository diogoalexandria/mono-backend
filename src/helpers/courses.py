from typing import Any, Union
from src.schemas.courses_schemas import CourseResponseSchema, CourseSchema

def response_course(course: Union[CourseSchema, Any]) -> CourseResponseSchema:    
    return CourseResponseSchema(
        id=course.id,
        name=course.name        
    )