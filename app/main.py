from fastapi import FastAPI
from app.api.v1.router import router as v1_router
from app.db.tables.users import create_users_table

app = FastAPI(title="FastAPI Social Network")


app.include_router(router=v1_router, prefix="/v1")


create_users_table()
