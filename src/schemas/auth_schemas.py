from pydantic import BaseModel, Field

class AuthRequestSchema(BaseModel):
    identity: str = Field(..., example="foo_bar@email.com")
    password: str = Field(..., example="Str0ngP@ssw0rd")   

