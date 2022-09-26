from fastapi import APIRouter
from fastapi import status, HTTPException
from schemas.posts import Post as PostSchema
from uuid import uuid4 as uuid
from fastapi.responses import JSONResponse
from models.posts import engine, session
from models.posts import Post as PostModel
from datetime import datetime

post = APIRouter()
posts = []
engine_local = engine
session_local = session


@post.get("/")
async def root():
    return "welcome to mi FastApi"


@post.get("/posts")
async def get_posts():
    return session_local.query(PostModel).all()


@post.post('/posts')
async def create_posts(post_api: PostSchema):
    create_post = PostModel(
        id=str(uuid()),
        title=post_api.title,
        author=post_api.author,
        content=post_api.content,
        created_at=datetime.now(),
        published_at=post_api.published_at,
        published=post_api.published

    )
    session_local.add(create_post)
    session_local.commit()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Post Created successfully"}
    )


@post.get('/posts/{post_id}')
async def get_post(post_id: str):
    getting_posts = session_local.query(PostModel).get(post_id)
    if getting_posts is not None:
        return getting_posts
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@post.delete('/posts/{post_id}')
async def delete_post(post_id: str):
    get_post_id = session_local.query(PostModel).get(post_id)
    if get_post_id is not None:
        session_local.query(PostModel).filter(PostModel.id == post_id).delete()
        session_local.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"detail": "Post has been deleted successfully"}
        )
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@post.put("/posts/{post_id}")
async def update_post(post_id: str, update_post: PostSchema):
    get_data = session_local.query(PostModel).get(post_id)
    if get_data is not None:
        session_local.query(PostModel).filter(PostModel.id == post_id).update(
            {
                "title": update_post.title,
                "author": update_post.author,
                "content": update_post.content,
                "published_at": datetime.now(),
                "published": True
            }
        )
        session_local.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"detail": "Post has been updated successfully"}
        )
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
