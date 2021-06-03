from src.schemas.status_schema import StatusOptions
from typing import Dict, Union
from fastapi import HTTPException
from src.helpers.courses import response_course
from sqlalchemy.orm.session import Session
from src.schemas.list_schema import ListRequestSchema
from src.models.courses_model import CoursesModel
from src.schemas.courses_schemas import CourseBaseSchema
from src.repositories.courses_repository import CoursesRepository

class CoursesService():
    def create_course( self, db: Session, *, object: CourseBaseSchema ):
       course = CoursesRepository.create(db, req_object=object)

       return response_course(course)


    def create_courses_list( self, db: Session, *, config: ListRequestSchema ):        
        skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        courses = CoursesRepository.get_all(db, skip=skip, limit=limit)
        
        response_course = []
        for course in courses:
            response_course.append(response_course(course))
        
        return response_course


    def validate_id( self, db: Session, *, id: str = id ) -> CoursesModel:
        user = CoursesRepository.get_by_id( db, id=id )
        if not user:        
            raise HTTPException( status_code=400, detail="Curso não encontrado." )

        return response_course(user)


    def update_course(

        self,
        db: Session,
        *,
        db_object: CoursesModel,
        infos_object: Union[CourseBaseSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        infos_object['id'] = id        

        updated_user = CoursesRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_course(updated_user)

    def remove_course( self, db: Session, *, id: str = id ):
        removed_user = CoursesRepository.remove(db, id=id)

        return response_course(removed_user)


CoursesService = CoursesService()