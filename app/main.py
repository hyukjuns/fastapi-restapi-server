import os, socket
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Set Version
VERSION="v1"

# Init App
app = FastAPI()

# Define Class
class Article(BaseModel):
    author: str
    title: str
    contents: str | None = None

# Default Article
first = Article(
    author="user1",
    title="default",
    contents="default content"
)

# Fake DB
article_list = [first]

# GET - Read articles
@app.get("/articles")
async def list_articles():
    return article_list

# GET - Read article one item
@app.get("/articles/{id}")
async def read_article(id: int = None):
    try:
        return article_list[id]
    except TypeError as e:
        raise HTTPException(status_code=404, detail=f"Article are empty!")
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f"Item not found!")

# article - Create
@app.post("/articles", response_model=Article, status_code=201)
async def create_article(article: Article):
    for data in article_list:
        if article.title == data.title:
            raise HTTPException(status_code=400, detail=f"Title aleady exists!")
    article_list.append(article)
    return article

# PUT - Update
@app.put("/articles/{id}")
async def update_article(id: int, article: Article):
    try:
        article_list[id].author = article.author
        article_list[id].title = article.title
        article_list[id].contents = article.contents
        return article_list
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f"Item not found!")

# DELETE - Delete
@app.delete("/articles/{id}")
async def delete_article(id: int):
    try:
        target = article_list[id]
        article_list.remove(target)
        return article_list
    except IndexError as e:
        raise HTTPException(status_code=404, detail=f"Item not found!")

# Check Healthy
@app.get("/")
async def hostname():
    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
        hostname = os.environ.get("HOSTNAME")
        return f"Version: {VERSION} hello from {hostname}"
    else:
        hostname = socket.gethostname()
        return f"Version: {VERSION} hello from {hostname}"

# Check Readiness
@app.get("/ready")
async def ready():
    return f"Version: {VERSION}, Application can response"

# Check Startup
@app.get("/connections")
async def connections_db():
    return f"Version: {VERSION}, Database Connection OK"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True, access_log=True)