from typing import Any, Dict, List, Union
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.services.auth_service import AuthService
from src.services.classes_service import ClassesService
from src.schemas.classes_schemas import ClassBaseSchema, ClassResponseSchema

router = APIRouter()

@router.post('/classes', response_model=ClassResponseSchema, status_code=201)
def create_class( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_class: ClassBaseSchema ) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    # ClassesService.validate_name(db, name=new_class.name)

    created_class = ClassesService.create_class(db, object=new_class)
    
    return created_class


@router.get('/classes', response_model=List[ClassResponseSchema])
def list_classes( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    classes_list = ClassesService.create_classes_list(db)

    return classes_list


@router.get('/classes_professor', response_model=List[ClassResponseSchema])
def list_classes_professor( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    classes_list = ClassesService.create_classes_by_professor(db, id=income_id)
    return classes_list


@router.get('/classes/{id}', response_model=ClassResponseSchema)
def list_class( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    class_item = ClassesService.validate_id(db, id=id)
    
    return class_item["response"]    
    

@router.patch('/classes/{id}', response_model=ClassResponseSchema, status_code=202)
def update_class(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[ClassBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_course = ClassesService.validate_id(db, id=id)
    updated_course = ClassesService.update_class(
        db,
        db_object=current_course["db_object"],
        infos_object=new_infos
    )
    
    return updated_course


@router.delete('/classes/{id}', response_model=ClassResponseSchema)
def remove_class( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)     
    removed_course = ClassesService.remove_class(db, id=id)

    return removed_course
    