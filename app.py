import uvicorn
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import logging

# Setting Logging 
logger = logging.getLogger(__name__)

# Init App
app = FastAPI()

# Define Class
class Post(BaseModel):
    publisher: str
    title: str
    contents: str | None = None

# Fake DB
post_list = []

# GET - Read
@app.get("/posts", status_code=200)
def list_post():
    logger.info("touched /posts")
    try:
        return post_list
    except HTTPException as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail="Item not found")

# @app.get("/teams/first", status_code=200)
# @app.get("/teams/last", status_code=200)
# @app.get("/teams/{id}", status_code=200)

# POST - Create
@app.post("/posts", status_code=201)
def create_post(post: Post):
    try:
        post_list.append(post)
        return post
    except HTTPException as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail="Item not found")

# PUT - Update
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    try:
        post_list[id] = post
        return post_list
    except HTTPException as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail="Item not found")

# DELETE - Delete
@app.delete("/posts/{id}")
def delete_post(id: int):
    try:
        target = post_list[id]
        post_list.remove(target)
        return post_list
    except Exception as e:
        logger.info(e)
        raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run("app:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level="debug", 
                reload=True, 
                access_log=True)