from fastapi import APIRouter
from fastapi import status, HTTPException
from models.models import Post
from uuid import uuid4 as uuid
from fastapi.responses import JSONResponse


post = APIRouter()
posts = []


@post.get("/")
async def root():
    return "welcome to mi FastApi"


@post.get("/posts")
async def show_posts():
    return posts


@post.post('/posts')
async def save_posts(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Post Created successfully"}
    )
    # return {"detail": "Post Created successfully", "status_code": status.HTTP_201_CREATED}


@post.get('/posts/{post_id}')
async def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@post.delete('/posts/{post_id}')
async def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"detail": "Post has been deleted successfully"}
            )
            # return {"detail": "Post has been deleted successfully", "status_code": status.HTTP_200_OK}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@post.put("/posts/{post_id}")
async def update_post(post_id: str, update_post: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = update_post.title
            posts[index]["content"] = update_post.content
            posts[index]["author"] = update_post.author
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"detail": "Post has been updated successfully"}
            )
            # return {"detail": "Post has been updated successfully", "status_code": status.HTTP_200_OK}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
