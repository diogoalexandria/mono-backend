from src.schemas.classes_schemas import ClassBaseSchema
from src.models.classes_model import ClassesModel
from src.helpers.classes import response_class
from src.repositories.classes_repository import ClassesRepository
from src.schemas.status_schema import StatusOptions
from typing import Dict, Union
from fastapi import HTTPException
from sqlalchemy.orm.session import Session

class ClassesService():
    def create_class( self, db: Session, *, object: ClassBaseSchema ):
       class_item = ClassesRepository.create(db, req_object=object)

       return response_class(class_item)


    def create_classes_list( self, db: Session ):        
        # skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        classes = ClassesRepository.get_all(db)
        
        response_classes = [response_class(class_item) for class_item in classes]
        
        return response_classes

    def validate_name( self, db: Session, *, name: str ):
        name_exist = ClassesRepository.get_by_name(db, name=name)
        if name_exist:
            raise HTTPException( status_code=400, detail="O nome já está cadastrado." )


    def validate_id( self, db: Session, *, id: str = id ) -> ClassesModel:
        class_item = ClassesRepository.get_by_id( db, id=id )
        if not class_item:        
            raise HTTPException( status_code=400, detail="Turma não encontrado." )
        
        return {
            "db_object": class_item,
            "response": response_class(class_item)
        }

    def create_classes_by_professor( self, db: Session, *, id: str = id ):
        classes = ClassesRepository.get_by_professor_id( db, id=id )
        response_classes = [response_class(class_item) for class_item in classes]
        
        return response_classes


    def update_class(

        self,
        db: Session,
        *,
        db_object: ClassesModel,
        infos_object: Union[ClassBaseSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        # infos_object['id'] = id        

        updated_class = ClassesRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_class(updated_class)

    def remove_class( self, db: Session, *, id: str = id ):               
        removed_class = ClassesRepository.remove(db, id=id)

        return response_class(removed_class)


ClassesService = ClassesService()