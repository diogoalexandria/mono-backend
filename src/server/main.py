from fastapi import FastAPI
#from starlette.middleware.cors import CORSMiddleware
from db.database import database
from routes import router

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    title="Educational Institution control",
    description="Api to control a education institution",
    version="1.0",
    openapi_url="/api/v/openapi.json"    
)

#@app.on_event("startup")
#async def startup():
#    await database.connect()

#app.on_event("shutdown")
#async def shutdown():
#    await database.disconnect()

app.include_router(router, prefix="/api/v1")