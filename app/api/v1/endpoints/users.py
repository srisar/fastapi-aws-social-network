from fastapi import APIRouter

from app.core.config import settings
from app.db.client import get_dynamodb_resource

router = APIRouter()


@router.get("/")
async def get_users():
    """
    Return all users
    """

    resource = get_dynamodb_resource()
    table = resource.Table(settings.DYNAMODB_TABLE)

    return {"data": table.table_status}
