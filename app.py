import uvicorn
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import logging
# Setting Logging 
logger = logging.getLogger(__name__)

# Init App
app = FastAPI()

# Define Class
class Article(BaseModel):
    reporter: str
    title: str
    contents: str | None = None

# Fake DB
article_list = []

# GET - Read
@app.get("/articles", status_code=200)
def list_article(idx: int = None):
    if idx:
        try:
            return article_list[idx]
        except IndexError as e:
            raise HTTPException(status_code=404, detail=e)
    else:
        return article_list

# article - Create
@app.post("/articles", status_code=201)
def create_article(article: Article):
    for idx, data in enumerate(article_list):
        if article.title == data.title:
            raise HTTPException(status_code=400, detail=f"Title aleady exists! index is {idx}")
    else:
        article_list.append(article)
        return article

# PUT - Update
@app.put("/articles/{id}")
def update_article(id: int, article: Article):
    try:
        article_list[id].reporter = article.reporter
        article_list[id].title = article.title
        article_list[id].contents = article.contents
        return article_list
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f"Item not found!  Error Message: {str(e)}")

# DELETE - Delete
@app.delete("/articles/{id}")
def delete_article(id: int):
    try:
        target = article_list[id]
        article_list.remove(target)
        return article_list
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f"Item not found! Error Message: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("app:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level="debug", 
                reload=True, 
                access_log=True)