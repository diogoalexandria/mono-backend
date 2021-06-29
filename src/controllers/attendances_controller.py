from src.services.attendances_service import AttendancesService
from src.schemas.attendances_schemas import AttendanceBaseSchema, AttendanceResponseSchema, AttendanceTopicResponseSchema, AttendancesListSchema
from src.services.auth_service import AuthService
from typing import Any, Dict, List, Union
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.helpers.auth import Auth
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post('/attendances', response_model=List[AttendanceResponseSchema], status_code=201)
def create_attendance( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_attendance: AttendancesListSchema ) -> Any:
    AuthService.validate_professor_access(db, id=income_id)
    
    # ClassesService.validate_name(db, name=new_class.name)

    created_attendances = AttendancesService.create_attendances(db, object=new_attendance)
    
    return created_attendances
    

@router.get('/attendances', response_model=List[AttendanceResponseSchema])
def list_attendances( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    attendances_list = AttendancesService.create_attendances_list(db)

    return attendances_list


@router.get('/attendances_topic/{id}', response_model=List[AttendanceTopicResponseSchema])
def list_attendances_topic( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:    
    topics_list = AttendancesService.create_attendance_list_by_topic(db, id=id)

    return topics_list


@router.get('/attendances/{id}', response_model=AttendanceResponseSchema)
def list_topic( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:    
    topic = AttendancesService.validate_id(db, id=id)
    
    return topic["response"]
    

@router.patch('/attendances/{id}', response_model=AttendanceResponseSchema, status_code=202)
def update_topic(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[AttendanceBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_attendance = AttendancesService.validate_id(db, id=id)
    updated_attendance = AttendancesService.update_attendance(
        db,
        db_object=current_attendance["db_object"],
        infos_object=new_infos
    )
    
    return updated_attendance


@router.delete('/attendances/{id}', response_model=AttendanceResponseSchema)
def remove_attendance( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)
       
    removed_attendance = AttendancesService.remove_attendance(db, id=id)

    return removed_attendance
