import os
import logging
import socket
from fastapi import FastAPI

app = FastAPI()

# GET
@app.get("/api/v1/info")
async def main(name: str = None):

    # Get hostname
    hostname = socket.gethostname()
    print(name)
    if name is not None:
        return {
                    "hostname": f"{hostname}",
                    "Your Name": f"{name}"

                }
    else:
        return {"hostname": f"{hostname}"}
