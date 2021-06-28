from src.schemas.topics_schemas import TopicBaseSchema, TopicProfessorResponseSchema, TopicResponseSchema
from typing import Any, Dict, List, Union
from fastapi import APIRouter, Depends
from src.helpers.auth import Auth
from src.database.session import db_session
from sqlalchemy.orm.session import Session
from src.services.auth_service import AuthService
from src.services.topics_service import TopicsService

router = APIRouter()

@router.post('/topics', response_model=TopicResponseSchema, status_code=201)
def create_topic( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), new_topic: TopicBaseSchema ) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    # ClassesService.validate_name(db, name=new_class.name)

    created_topic = TopicsService.create_topic(db, object=new_topic)
    
    return created_topic


@router.get('/topics', response_model=List[TopicResponseSchema])
def list_topics( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    topics_list = TopicsService.create_topics_list(db)

    return topics_list


@router.get('/topics', response_model=List[TopicResponseSchema])
def list_topics( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    topics_list = TopicsService.create_topics_list(db)

    return topics_list


@router.get('/topics_professor', response_model=List[TopicProfessorResponseSchema])
def list_topics_professor( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session) ) -> Any:
    topics_list = TopicsService.create_topics_list_by_professor(db, id=income_id)

    return topics_list


@router.get('/topics/{id}', response_model=TopicResponseSchema)
def list_topic( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ) -> Any:
    topic = TopicsService.validate_id(db, id=id)
    
    return topic["response"]
    

@router.patch('/topics/{id}', response_model=TopicResponseSchema, status_code=202)
def update_topic(

    income_id=Depends(Auth.wrapper),
    *,
    db: Session = Depends(db_session),
    new_infos: Union[TopicBaseSchema,  Dict[str, str]],
    id: str = id 
    
) -> Any:
    AuthService.validate_admin_access(db, id=income_id)
    
    current_topic = TopicsService.validate_id(db, id=id)
    updated_topic = TopicsService.update_topic(
        db,
        db_object=current_topic["db_object"],
        infos_object=new_infos
    )
    
    return updated_topic


@router.delete('/topics/{id}', response_model=TopicResponseSchema)
def remove_topic( income_id = Depends(Auth.wrapper), *, db: Session = Depends(db_session), id: str = id ):
    AuthService.validate_admin_access(db, id=income_id)
       
    removed_topic = TopicsService.remove_topic(db, id=id)

    return removed_topic
