from fastapi import APIRouter
from app.api.v1.endpoints import users, profiles

router = APIRouter()

router.include_router(router=users.router, prefix="/users", tags=["users"])
router.include_router(router=profiles.router, prefix="/profiles", tags=["profiles"])
