from src.schemas.attendances_schemas import AttendanceResponseSchema, AttendanceSchema
from typing import Any, Union
from src.schemas.courses_schemas import CourseResponseSchema, CourseSchema

def response_attendance(attendance: Union[AttendanceSchema, Any]) -> AttendanceResponseSchema:
        
    return AttendanceResponseSchema(
        id=attendance.id,
        topic_id=attendance.topic_id,
        student_id=attendance.student_id        
    )