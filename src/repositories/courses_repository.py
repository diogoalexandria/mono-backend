from src.schemas.courses_schema import CourseBaseSchema
from src.repositories.base_repository import BaseRepository
from src.models.courses_model import CoursesModel

class CoursesRepository( BaseRepository[CoursesModel, CourseBaseSchema, CourseBaseSchema] ):
    pass

CoursesRepository = CoursesRepository( CoursesModel )