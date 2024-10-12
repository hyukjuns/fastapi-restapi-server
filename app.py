import os
import socket
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()

# Welcome Page
@app.get("/", status_code=200)
def welcome(request: Request, response_class=HTMLResponse):

    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
        hostname = os.environ.get("HOSTNAME")
        
    else:
        hostname = socket.gethostname()
    
    header_list = ""
    for item in request.headers.items():
        header_list += f"{item[0]}: {item[1]}<br>"
    
    html_content = f"""
                <html>
                    <head>
                        <title> Welcome Page </title>
                    </head>
                    <body>
                        <h1> Welcome to my player info server </h1>
                        <p>
                            - <strong>Server Hostname:</strong> {hostname} <br>
                            - <strong>Client Information:</strong>:  <br>
                            - <strong>request_header:</strong> {header_list}
                            - <strong>request_method:</strong> {request.method} <br>
                            - <strong>request_address:</strong> {request.client} <br>
                            - <strong>request_path_params:</strong> {request.path_params} <br>
                            - <strong>request_query_params:</strong> {request.query_params} <br>
                            - <strong>request_url:</strong> {request.url}
                        </p>
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