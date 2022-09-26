from fastapi import FastAPI
from routes.post import post


description = """
Posts API helps you do awesome stuff. 🚀

## Items

You can create, update, delete, show all post you've made

"""

app = FastAPI(
    title="Posts APi",
    description=description,
    version="1.1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Eliecer Aguilar",
        "url": "https://www.linkedin.com/in/eliecer-aguilar-507/",
        "email": "elieaguilar91@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(post)
