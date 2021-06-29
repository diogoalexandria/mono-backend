from src.schemas.attendances_schemas import AttendanceResponseSchema, AttendanceSchema, AttendanceTopicResponseSchema
from typing import Any, Union
from src.schemas.courses_schemas import CourseResponseSchema, CourseSchema

def response_attendance(attendance: Union[AttendanceSchema, Any]) -> AttendanceResponseSchema:
        
    return AttendanceResponseSchema(
        id=attendance.id,
        topic_id=attendance.topic_id,
        student_id=attendance.student_id        
    )

def response_attendance_topic(result: Union[AttendanceSchema, Any]) -> AttendanceTopicResponseSchema:
    attendance, users = result     
    return AttendanceTopicResponseSchema(
        student_id=users.id,
        first_name=users.first_name,
        last_name=users.last_name        
    )