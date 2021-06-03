from src.services.subjects_service import SubjectsService
from typing import Any, Dict, List, Union
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.schemas.list_schema import ListRequestSchema
from src.services.auth_service import AuthService
from src.schemas.subjects_schemas import SubjectBaseSchema, SubjectResponseSchema

router = APIRouter()

@router.post('/subjects', response_model=SubjectResponseSchema, status_code=201)
def create( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_course: SubjectBaseSchema ) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    created_course = SubjectsService.create_course(db, object=new_course)
    
    return created_course


@router.get('/subjects', response_model=List[SubjectResponseSchema])
def list_courses( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session),  config: ListRequestSchema ) -> Any:
    courses_list = SubjectsService.create_courses_list()

    return courses_list


@router.get('/subjects/{id}', response_model=SubjectResponseSchema)
def list_course( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    course = SubjectsService.validate_id(db, id=id)
    
    return course
    

@router.patch('/subjects/{id}', response_model=SubjectResponseSchema, status_code=202)
def update(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[SubjectBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_course = SubjectsService.validate_id(db, id=id)
    updated_course = SubjectsService.update_course(db, db_object=current_course, infos_object=new_infos)
    
    return updated_course


@router.delete('/subjects/{id}', response_model=SubjectResponseSchema)
def remove( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)

    removed_course = SubjectsService.remove_course()

    return removed_course