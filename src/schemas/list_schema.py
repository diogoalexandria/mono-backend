from typing import Optional
from pydantic import BaseModel, Field

class ListRequestSchema(BaseModel):
    skip:  Optional[int] = Field(example=0)
    limit: Optional[int] = Field(example=100)