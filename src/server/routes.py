from fastapi import APIRouter

from src.controllers import users_controller

router = APIRouter()

@router.get("/health")
def health_checker():
    return { "status": "up"}

router.include_router(users_controller.router, prefix="/users", tags=["users"])
#router.include_router(login.router, tags=["login"])
#router.include_router(utils.router, prefix="/utils", tags=["utils"])
#router.include_router(items.router, prefix="/items", tags=["items"])