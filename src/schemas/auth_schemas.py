from pydantic import BaseModel, Field
from sqlalchemy.sql.sqltypes import String

class AuthRequestSchema(BaseModel):
    identity: str = Field(..., example="foo_bar@email.com")
    password: str = Field(..., example="Str0ngP@ssw0rd")   

class TokenResponseSchema(BaseModel):
    token: str = Field(..., example="t0Kente5T")
    