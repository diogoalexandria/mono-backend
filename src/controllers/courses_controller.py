from src.schemas.list_schema import ListRequestSchema
from typing import Any, Dict, List, Union
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.schemas.courses_schema import CourseBaseSchema, CourseResponseSchema

router = APIRouter()

@router.post('/courses', response_model=CourseResponseSchema, status_code=201)
def create( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_user: CourseBaseSchema ) -> Any:
    
    pass

@router.get('/courses', response_model=List[CourseResponseSchema])
def list_courses( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session),  config: ListRequestSchema ) -> Any:
    pass

@router.get('/courses/{id}', response_model=CourseResponseSchema)
def list_course( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    pass

@router.patch('/courses/{id}', response_model=CourseResponseSchema, status_code=202)
def update(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[CourseBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    pass

@router.delete('/courses/{id}', response_model=CourseResponseSchema)
def remove( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    pass