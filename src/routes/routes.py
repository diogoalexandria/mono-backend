from fastapi import APIRouter

from src.controllers import health_controller
from src.controllers import auth_controller
from src.controllers import users_controller
from src.controllers import courses_controller
from src.controllers import subjects_controller
from src.controllers import subscriptions_controller
from src.controllers import classes_controller
from src.controllers import topics_controller
from src.controllers import attendances_controller

router = APIRouter()

router.include_router(health_controller.router, prefix="/v1", tags=["Health"])
router.include_router(auth_controller.router, prefix="/v1", tags=["Auth"])
router.include_router(users_controller.router, prefix="/v1", tags=["Users"])
router.include_router(courses_controller.router, prefix="/v1", tags=["Courses"])
router.include_router(subjects_controller.router, prefix="/v1", tags=["Subjects"])
router.include_router(classes_controller.router, prefix="/v1", tags=["Classes"])
router.include_router(subscriptions_controller.router, prefix="/v1", tags=["Subscriptions"])
router.include_router(topics_controller.router, prefix="/v1", tags=["Topics"])
router.include_router(attendances_controller.router, prefix="/v1", tags=["Attendances"])
