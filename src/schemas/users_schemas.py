from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy.sql.sqltypes import Enum
from src.schemas.status_schema import StatusOptions

class UsersEntities(str, Enum):
    administrator= "administrator"
    professor= "professor"
    student= "student"
    
class UserBaseSchema(BaseModel):
    email:      Optional[str]           = Field(example="foo_bar@email.com")
    username:   Optional[str]           = Field(example="foo.bar")
    first_name: Optional[str]           = Field(example="Foo")
    last_name:  Optional[str]           = Field(example="Bar")    
    gender:     Optional[str]           = Field(example="Male", default=None)
    entity:     Optional[UsersEntities] = Field(example="student")

class UserUpdateSchema(UserBaseSchema):
    password:   Optional[str]           = Field( example="Str0ngP@ssw0rd")
    status:     Optional[StatusOptions] = Field( example="active") 

class UserResponseSchema(UserBaseSchema):
    id:         UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    email:      str                     = Field(..., example="foo_bar@email.com")
    entity:     UsersEntities           = Field(..., example="student")
    username:   str                     = Field(..., example="foo.bar")
    first_name: str                     = Field(..., example="Foo")
    last_name:  str                     = Field(..., example="Bar")
    status:     StatusOptions           = Field(..., example="active")       

class UserRequestSchema(UserBaseSchema):
    email:      str                     = Field(..., example="foo_bar@email.com")
    username:   str                     = Field(..., example="foo.bar")
    password:   str                     = Field(..., example="Str0ngP@ssw0rd")
    first_name: str                     = Field(..., example="Foo") 
    last_name:  str                     = Field(..., example="Bar")
    entity:     UsersEntities           = Field(..., example="student")   

class UserSchema(UserRequestSchema):
    id:         UUID                    = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    status:     str                     = Field(..., example="active")  
    created_at: str                     = Field(..., example="2025-12-19 09:26:03.478039")
    updated_at: Optional[str]           = Field(example="2025-12-19 09:26:03.478039")

    class Config:
        orm_mode = True