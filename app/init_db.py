from app.db import engine
from app.models import SQLModel

def init_db():
    SQLModel.metadata.create_all(engine)
    print("✅ Database initialized")

if __name__ == "__main__":
    init_db()
