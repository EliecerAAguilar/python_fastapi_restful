from fastapi import FastAPI, status, HTTPException
from models.models import Post
from uuid import uuid4 as uuid


app = FastAPI()
posts = []


@app.get("/")
async def root():
    return "welcome to mi FastApi"


@app.get("/posts")
async def show_posts():
    return posts

@app.post('/posts')
async def save_posts(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return status.HTTP_201_CREATED


@app.get('/posts/{post_id}')
async def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.delete('/posts/{post_id}')
async def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"detail": "Post has been deleted successfully", "status_code": status.HTTP_200_OK}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


