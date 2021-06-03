from typing import Any, Union
from src.schemas.courses_schemas import CourseBaseSchema, CourseSchema

def response_course(course: Union[CourseSchema, Any]) -> CourseBaseSchema:    
    return CourseBaseSchema(
        name=course.name        
    )