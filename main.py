from config.desencrypt import DbConnection
from fastapi import FastAPI
from routes.post import post

app = FastAPI()
app.include_router(post)
connection = DbConnection()
connection.engine_connection()




