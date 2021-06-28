from src.models.topics_model import TopicsModel
from src.repositories.topics_repository import TopicsRepository
from src.helpers.topics import response_topic, response_topic_professor
from src.schemas.topics_schemas import TopicBaseSchema
from src.schemas.status_schema import StatusOptions
from typing import Dict, Union
from fastapi import HTTPException
from sqlalchemy.orm.session import Session

class TopicsService():
    def create_topic( self, db: Session, *, object: TopicBaseSchema ):
        topic = TopicsRepository.create(db, req_object=object)
        
        return response_topic(topic)


    def create_topics_list( self, db: Session ):        
        # skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        topics = TopicsRepository.get_all(db)
        
        response_topics = [response_topic(topic) for topic in topics]
        
        return response_topics


    def create_topics_list_by_professor(self, db: Session, *, id: str = id):
        topics = TopicsRepository.get_by_professor(db, id=id)

        response_topics = [response_topic_professor(topic) for topic in topics]
        
        return response_topics        


    def validate_name( self, db: Session, *, name: str ):
        name_exist = TopicsRepository.get_by_name(db, name=name)
        if name_exist:
            raise HTTPException( status_code=400, detail="O nome já está cadastrado." )


    def validate_id( self, db: Session, *, id: str = id ) -> TopicsModel:
        topic = TopicsRepository.get_by_id( db, id=id )
        if not topic:        
            raise HTTPException( status_code=400, detail="Aula não encontrado." )
        
        return {
            "db_object": topic,
            "response": response_topic(topic)
        }


    def update_topic(

        self,
        db: Session,
        *,
        db_object: TopicsModel,
        infos_object: Union[TopicBaseSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        # infos_object['id'] = id        

        updated_topic = TopicsRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_topic(updated_topic)

    def remove_topic( self, db: Session, *, id: str = id ):                
        removed_topic = TopicsRepository.remove(db, id=id)

        return response_topic(removed_topic)


TopicsService = TopicsService()
