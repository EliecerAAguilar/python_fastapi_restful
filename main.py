from fastapi import FastAPI, status, HTTPException
from models.models import Post
from uuid import uuid4 as uuid
from fastapi.responses import JSONResponse
from config.desencrypt import DbConnection


app = FastAPI()
posts = []
connection = DbConnection()
connection.engine_connection()

# engine = create_engine(f'{DB_MANAGEMENT_SYSTEM}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')


