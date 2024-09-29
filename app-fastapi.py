import os
import logging
import socket
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()

@app.get("/api/v1/hostname")
def get_hostname(request: Request):

    request_info = {
        'request_header': request.headers,
        'request_method': request.method,
        'request_address': request.client,
        'request_path_params': request.path_params,
        'request_query_params': request.query_params,
        'request_url': request.url
    }
    json_compatible_item_data = jsonable_encoder(request_info)
    # Get hostname
    if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
        pod_name = os.environ.get("HOSTNAME")
        return {
            "hostname": f"{pod_name}",
            "requsts": f"{json_compatible_item_data}"
            }
    else:
        local_hostname = socket.gethostname()
        return {
            "hostname": f"{local_hostname}", 
            "requsts": f"{json_compatible_item_data}"
            }

# @app.get("/api/v1/hostname")
# async def get_hostname(name: str = None):

#     # Get hostname
#     hostname = socket.gethostname()
#     print(name)
#     if name is not None:
#         return {
#                     "hostname": f"{hostname}",
#                     "Your Name": f"{name}"
#                 }
#     else:
#         return {"hostname": f"{hostname}"}
