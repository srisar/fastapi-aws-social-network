from pprint import pprint

from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="FastAPI Social Network")


pprint(settings.json())
