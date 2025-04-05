import os, socket
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Note
from app.db import SessionLocal
import os

# Set Version
VERSION="v1"

# Init App
app = FastAPI()


# DB Session 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /notes 모든 메모 조회
@app.get("/notes")
def list_note(db: Session = Depends(get_db)):
    return db.query(Note).all()

# # GET /notes/{id} 특정 메모 조회
# @app.get("/notes/{id}",  response_model=Note)
# def get_note(id: int):
#     for note in fake_notes_db:
#         if note.id == id:
#             return note
#     raise HTTPException(status_code=404, detail=f"Note Not Found!")


# # POST /notes 새 메모 추가
# @app.post("/notes", response_model=dict)
# def create_note(new_note: Note):
#     for note in fake_notes_db:
#         if note.id == new_note.id:
#             raise HTTPException(status_code=400, detail=f"ID Aleady Exists!")
#     fake_notes_db.append(new_note)
#     return {"message": "Create Operation Completed", "created_note": new_note}

# # PUT /notes/{id} 메모 수정
# @app.put("/notes/{id}", response_model=dict)
# def update_note(id: int, updated_note: Note):
#     for index, note in enumerate(fake_notes_db):
#         if note.id == id:
#             fake_notes_db[index] = updated_note
#             return {"message": "Update Operation Completed", "updated_note": updated_note}
#     raise HTTPException(status_code=404, detail=f"Note Not Found!")

# # DELETE /notes/{id} 메모 삭제
# @app.delete("/notes/{id}")
# def delete_note(id: int):
#     for index, note in enumerate(fake_notes_db):
#         if note.id == id:
#             fake_notes_db.pop(index)
#             return {"message": "Delete Operation Completed", "current_notes": fake_notes_db}
#     raise HTTPException(status_code=404, detail=f"Note Not Found!")

# # Check Healthy
# @app.get("/")
# def hostname():
#     if os.path.exists('/var/run/secrets/kubernetes.io/serviceaccount') or os.getenv('KUBERNETES_SERVICE_HOST') is not None:
#         hostname = os.environ.get("HOSTNAME")
#         return f"Version: {VERSION} hello from {hostname}"
#     else:
#         hostname = socket.gethostname()
#         return f"Version: {VERSION} hello from {hostname}"

# # Check Readiness
# @app.get("/ready")
# def ready():
#     return f"Version: {VERSION}, Application can response"

# # Check Startup
# @app.get("/connections")
# def connections_db():
#     return f"Version: {VERSION}, Database Connection OK"


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="debug", reload=True, access_log=True)