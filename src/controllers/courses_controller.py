from typing import Any, Dict, List, Union
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.schemas.list_schema import ListRequestSchema
from src.services.auth_service import AuthService
from src.schemas.courses_schemas import CourseBaseSchema, CourseResponseSchema
from src.services.courses_service import CoursesService

router = APIRouter()

@router.post('/courses', response_model=CourseResponseSchema, status_code=201)
def create_course( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_course: CourseBaseSchema ) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    CoursesService.validate_name(db, name=new_course.name)

    created_course = CoursesService.create_course(db, object=new_course)
    
    return created_course


@router.get('/courses', response_model=List[CourseResponseSchema])
def list_courses( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    courses_list = CoursesService.create_courses_list(db)

    return courses_list


@router.get('/courses/{id}', response_model=CourseResponseSchema)
def list_course( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    course = CoursesService.validate_id(db, id=id)
    
    return course["response"]
    

@router.patch('/courses/{id}', response_model=CourseResponseSchema, status_code=202)
def update_course(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[CourseBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_course = CoursesService.validate_id(db, id=id)
    updated_course = CoursesService.update_course(
        db,
        db_object=current_course["db_object"],
        infos_object=new_infos
    )
    
    return updated_course


@router.delete('/courses/{id}', response_model=CourseResponseSchema)
def remove_course( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)    
    removed_course = CoursesService.remove_course(db, id=id)

    return removed_course