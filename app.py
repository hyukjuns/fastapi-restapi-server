import os
import socket
import uvicorn
import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    name: str | None = None
    content: str | None = None

post_list = [] # Fake DB

# Read
@app.get("/posts", status_code=200)
def list_teams():
    return post_list

# @app.get("/teams/first", status_code=200)
# @app.get("/teams/last", status_code=200)
# @app.get("/teams/{id}", status_code=200)

# Create
@app.post("/posts", status_code=201)
def create_post(post: Post):
    print(post)
    post_list.append(post)
    return post

# Update
@app.put("/posts/{id}", status_code=200)
def update_post(id: int, post: Post):
    post_list[id] = post
    return 200

# Delete
@app.delete("/posts/{id}", status_code=200)
def delete_post(id: int):
    target = post_list[id]
    post_list.remove(target)
    return 200

# Welcome Page
@app.get("/", status_code=200)
def welcome(request: Request, response_class=HTMLResponse):

    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
        hostname = os.environ.get("HOSTNAME")
        
    else:
        hostname = socket.gethostname()
    
    header_list = ""
    for item in request.headers.items():
        header_list += f"<li>{item[0]}: {item[1]}</li>"
    
    html_content = f"""
                <html>
                    <head>
                        <title> Welcome Page </title>
                    </head>
                    <body>
                        <h1> Welcome to my sample FastAPI Server </h1>
                        <ul>
                            <li> <strong>Server Hostname:</strong> {hostname}</li> 
                            <li> <strong>Client Information:</strong> </li> 
                            <li> <strong>request_header:</strong> </li>
                                <ul>
                                    {header_list}
                                </ul> 
                            <li> <strong>request_method:</strong> {request.method}</li> 
                            <li> <strong>request_address:</strong> {request.client}</li> 
                            <li> <strong>request_path_params:</strong> {request.path_params}</li> 
                            <li> <strong>request_query_params:</strong> {request.query_params}</li> 
                            <li> <strong>request_url:</strong> {request.url} </li>
                        </ul>
                    </body>
                </html>
            """
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    uvicorn.run("app:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level="debug", 
                reload=True, 
                access_log=True)