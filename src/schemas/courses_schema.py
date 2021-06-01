from pydantic import BaseModel, Field

class CourseBaseSchema(BaseModel):
    name: str = Field(..., example="Math")
    