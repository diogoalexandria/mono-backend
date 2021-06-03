from src.schemas.status_schema import StatusOptions
from typing import Dict, Union
from fastapi import HTTPException
from src.helpers.subjects import response_subject
from sqlalchemy.orm.session import Session
from src.schemas.list_schema import ListRequestSchema
from src.models.subjects_model import SubjectsModel
from src.schemas.subjects_schemas import SubjectBaseSchema
from src.repositories.subjects_repository import SubjectsRepository

class SubjectsService():
    def create_subject( self, db: Session, *, object: SubjectBaseSchema ):
       subject = SubjectsRepository.create(db, req_object=object)

       return response_subject(subject)


    def create_subjects_list( self, db: Session, *, config: ListRequestSchema ):        
        skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        subjects = SubjectsRepository.get_all(db, skip=skip, limit=limit)
        
        response_subject = []
        for subject in subjects:
            response_subject.append(response_subject(subject))
        
        return response_subject


    def validate_id( self, db: Session, *, id: str = id ) -> SubjectsModel:
        user = SubjectsRepository.get_by_id( db, id=id )
        if not user:        
            raise HTTPException( status_code=400, detail="Curso não encontrado." )

        return response_subject(user)


    def update_subject(

        self,
        db: Session,
        *,
        db_object: SubjectsModel,
        infos_object: Union[SubjectBaseSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        infos_object['id'] = id        

        updated_user = SubjectsRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_subject(updated_user)

    def remove_subject( self, db: Session, *, id: str = id ):
        removed_user = SubjectsRepository.remove(db, id=id)

        return response_subject(removed_user)


SubjectsService = SubjectsService()