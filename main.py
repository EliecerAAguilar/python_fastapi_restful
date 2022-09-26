from fastapi import FastAPI
from routes.post import post


app = FastAPI()
app.include_router(post)
