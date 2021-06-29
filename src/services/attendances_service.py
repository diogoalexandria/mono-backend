from src.schemas.attendances_schemas import AttendanceBaseSchema, AttendancesListSchema
from src.models.attendances_model import AttendancesModel
from src.helpers.attendances import response_attendance, response_attendance_topic
from src.repositories.attendances_repository import AttendancesRepository
from src.schemas.status_schema import StatusOptions
from typing import Dict, Union
from fastapi import HTTPException
from sqlalchemy.orm.session import Session

class AttendancesService():
    def create_attendance( self, db: Session, *, object: AttendanceBaseSchema ):
        attendance = AttendancesRepository.create(db, req_object=object)
        
        return response_attendance(attendance)


    def create_attendances( self, db: Session, *, object: AttendancesListSchema ):
        attendances = AttendancesRepository.create_multi(db, req_object=object)
        
        response_attendances = [response_attendance(attendance) for attendance in attendances]
        
        return response_attendances


    def create_attendances_list( self, db: Session ):        
        # skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        attendances = AttendancesRepository.get_all(db)
        
        response_attendances = [response_attendance(attendance) for attendance in attendances]
        
        return response_attendances


    def create_attendance_list_by_topic( self, db: Session, *, id: str = id  ):        
        # skip, limit = dict(config).values() # Desestruturando (Unpacking) os valores do Request Body config
        attendances = AttendancesRepository.get_by_topic(db, id=id)
        
        response_attendances = [response_attendance_topic(attendance) for attendance in attendances]
        
        return response_attendances    


    def validate_id( self, db: Session, *, id: str = id ) -> AttendancesModel:
        attendance = AttendancesRepository.get_by_id( db, id=id )
        if not attendance:        
            raise HTTPException( status_code=400, detail="Aula não encontrado." )
        
        return {
            "db_object": attendance,
            "response": response_attendance(attendance)
        }


    def update_attendance(

        self,
        db: Session,
        *,
        db_object: AttendancesModel,
        infos_object: Union[AttendanceBaseSchema,  Dict[str, Union[str, StatusOptions]]]

    ):        
        # Reforçando que o id que chega no Params seja o mesmo que o Request Body
        # infos_object['id'] = id        

        updated_attendance = AttendancesRepository.update(db, db_object=db_object, req_object=infos_object)
        
        return response_attendance(updated_attendance)

    def remove_attendance( self, db: Session, *, id: str = id ):                
        removed_attendance = AttendancesRepository.remove(db, id=id)

        return response_attendance(removed_attendance)


AttendancesService = AttendancesService()