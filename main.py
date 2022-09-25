from fastapi import FastAPI
from models.models import Post

app = FastAPI()

posts = []
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/posts")
async def root():
    return posts


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post('/posts')
def save_posts(post: Post):
    posts.append(post.dict())
    return "recived"