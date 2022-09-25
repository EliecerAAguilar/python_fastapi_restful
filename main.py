from fastapi import FastAPI
from routes.post import post
from models import posts as models_posts

app = FastAPI()
app.include_router(post)
