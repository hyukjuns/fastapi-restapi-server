import os
import logging
import socket
import uvicorn
from fastapi import FastAPI, Request, HTTPException


app = FastAPI()

# Fake Key Value Database
fake_rank_db = {
        "son": 1, 
        "maddison": 2, 
        "solanke": 3
}

# Get Player's Ranking by Query Parameter
@app.get("/api/v1/ranks")
async def read_item(player: str = None, status_code=200):
    if player is None:
        return fake_rank_db
    if player not in fake_rank_db:
        raise HTTPException(status_code=404, detail="Player not found")
    return f"{player} is {fake_rank_db[player]} rank" 
 
# Get Host Name
@app.get("/api/v1/hostname", status_code=200)
def get_hostname():

    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
        pod_name = os.environ.get("HOSTNAME")
        return {
                "hostname": f"{pod_name}",
        }
    else:
        local_hostname = socket.gethostname()
        return {
                "hostname": f"{local_hostname}", 
        }

# Get Request Info
@app.get("/", status_code=200)
async def home(request: Request):

    request_info = {
        'request_header': request.headers,
        'request_method': request.method,
        'request_address': request.client,
        'request_path_params': request.path_params,
        'request_query_params': request.query_params,
        'request_url': request.url
    }

    return {
        "request info": f"{request_info}"
    }


if __name__ == "__main__":
    uvicorn.run("app:app", 
                host="0.0.0.0", 
                port=8000, 
                log_level="debug", 
                reload=True, 
                access_log=True)