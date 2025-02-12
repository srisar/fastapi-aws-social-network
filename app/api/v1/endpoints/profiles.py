from fastapi import APIRouter


router = APIRouter()


@router.get("/profiles")
async def get_profiles():
    return {
        "profiles": "profiles",
    }
