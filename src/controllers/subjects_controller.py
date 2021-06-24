from typing import Any, Dict, List, Union
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.schemas.list_schema import ListRequestSchema
from src.services.auth_service import AuthService
from src.schemas.subjects_schemas import SubjectBaseSchema, SubjectResponseSchema
from src.services.subjects_service import SubjectsService

router = APIRouter()

@router.post('/subjects', response_model=SubjectResponseSchema, status_code=201)
def create_subject( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_subject: SubjectBaseSchema ) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    created_subject = SubjectsService.create_subject(db, object=new_subject)
    
    return created_subject


@router.get('/subjects', response_model=List[SubjectResponseSchema])
def list_subjects( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    subjects_list = SubjectsService.create_subjects_list(db)

    return subjects_list


@router.get('/subjects/{id}', response_model=SubjectResponseSchema)
def list_subject( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    subject = SubjectsService.validate_id(db, id=id)
    
    return subject["response"]
    

@router.patch('/subjects/{id}', response_model=SubjectResponseSchema, status_code=202)
def update_subject(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[SubjectBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_subject = SubjectsService.validate_id(db, id=id)
    updated_subject = SubjectsService.update_subject(
        db,
        db_object=current_subject["db_object"],
        infos_object=new_infos
    )
    
    return updated_subject


@router.delete('/subjects/{id}', response_model=SubjectResponseSchema)
def remove_subject( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)

    removed_subject = SubjectsService.remove_subject(db, id=id)

    return removed_subject