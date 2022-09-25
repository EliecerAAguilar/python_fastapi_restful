from fastapi import FastAPI, status, HTTPException
from models.models import Post
from uuid import uuid4 as uuid
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
# from config.config import USER, PASSWORD, DB, PORT, HOST, DRIVER, DB_MANAGEMENT_SYSTEM
from cryptography.fernet import Fernet
import json
from config.encrypt import key as encripted_key

# Decryption Script .
# Use one of the methods to get a key ( it must be the same as used in encrypting )
key_file = 'config/key.txt'
print(encripted_key, "main.py")
input_file = 'config/encrypted'

with open(key_file, 'rb') as k:
    key = k.read()

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
decrypted = fernet.decrypt(data)
config = json.loads(decrypted)

# BUILD THE CONNECTION
engine = create_engine(
    URL(
        username=config["USER"],
        password=config["PASSWORD"],
        database=config["DB"],
        port=config["PORT"],
        host=config["HOST"],
        drivername=config["DRIVER_NAME"]
    )
)
# BUILD THE CONNECTION
connection = engine.connect()

app = FastAPI()
posts = []


# engine = create_engine(f'{DB_MANAGEMENT_SYSTEM}+{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')


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
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Post Created successfully"}
    )
    # return {"detail": "Post Created successfully", "status_code": status.HTTP_201_CREATED}


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
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"detail": "Post has been deleted successfully"}
            )
            # return {"detail": "Post has been deleted successfully", "status_code": status.HTTP_200_OK}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


@app.put("/posts/{post_id}")
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
