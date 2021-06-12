from fastapi import FastAPI
from src.routes import routes
from src.config import Settings
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(

    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    title="Educational Institution control",
    description="Api to control a education institution",
    version="1.0",
    openapi_url="/api/v/openapi.json" 

)

# origins = [
#     "http://localhost:5000",
# ]

# middleware = [
#     Middleware(CORSMiddleware, allow_origins=origins)
# ]

# app = FastAPI(middleware=middleware)

if Settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in Settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router( routes.router, prefix="/api" )