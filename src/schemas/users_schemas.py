import datetime
from typing import Optional
from pydantic import BaseModel, Field

class UserBaseSchema(BaseModel):
    email:      Optional[str] = Field(example="foo_bar@email.com")
    username:   Optional[str] = Field(example="foo.bar")
    first_name: Optional[str] = Field(example="Foo")
    last_name:  Optional[str] = Field(example="Bar")    
    gender:     Optional[str] = Field(example="Male", default=None)
    entity:     Optional[str] = Field(example="student")

class UserUpdateSchema(UserBaseSchema):
    password:   Optional[str] = Field(..., example="Str0ngP@ssw0rd")
    status:     Optional[str] = Field(..., example="active") 

class UserResponseSchema(UserBaseSchema):
    email:      str           = Field(..., example="foo_bar@email.com")
    username:   str           = Field(..., example="foo.bar")
    first_name: str           = Field(..., example="Foo")
    last_name:  str           = Field(..., example="Bar")    

class UserRequestSchema(UserBaseSchema):
    email:      str           = Field(..., example="foo_bar@email.com")
    username:   str           = Field(..., example="foo.bar")
    password:   str           = Field(..., example="Str0ngP@ssw0rd")
    first_name: str           = Field(..., example="Foo") 
    last_name:  str           = Field(..., example="Bar")
    entity:     str           = Field(..., example="student")   

class UserSchema(UserRequestSchema):
    id:         str           = Field(..., example="Str0ngP@ssw0rd")
    status:     str           = Field(..., example="active")  
    created_at: str           = Field(..., example="")
    updated_at: Optional[str] = Field(example="")

    class Config:
        orm_mode = True