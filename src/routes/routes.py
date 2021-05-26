from fastapi import APIRouter

from src.controllers import health_controller
from src.controllers import auth_controller
from src.controllers import users_controller
from src.controllers import courses_controller

router = APIRouter()

router.include_router(auth_controller.router, prefix="/v1", tags=["auth"])
router.include_router(health_controller.router, prefix="/v1", tags=["health"])
router.include_router(users_controller.router, prefix="/v1", tags=["user"])
router.include_router(courses_controller.router, prefix="/v1", tags=["course"])

#router.include_router(users_controller.router, prefix="/users", tags=["users"])
#router.include_router(login.router, tags=["login"])
#router.include_router(utils.router, prefix="/utils", tags=["utils"])
#router.include_router(items.router, prefix="/items", tags=["items"])