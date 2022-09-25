from config.desencrypt import DbConnection
from fastapi import FastAPI
from routes.post import post

app = FastAPI()
app.include_router(post)
connection = DbConnection()
connection.engine_connection()

# engine = create_engine(f'{DB_MANAGEMENT_SYSTEM}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')


