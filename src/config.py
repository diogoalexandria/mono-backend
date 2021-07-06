from pydantic import AnyHttpUrl, BaseSettings, validator
from typing import List, Union

class Settings(BaseSettings):
    PORT = 5700
    SECRET = ""
    DATABASE_URL = "postgresql://postgres:password@localhost/institution"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000", "http://eduty-frontend.s3-website-us-east-1.amazonaws.com", "https://d27vx3050bso8f.cloudfront.net"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

Settings = Settings()