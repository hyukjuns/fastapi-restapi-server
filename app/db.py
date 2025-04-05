from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
import os

# 환경변수로 설정 가능, 기본값은 로컬 MySQL
DATABASE_URL = os.getenv("DB_CONNECTION_STRING", "mysql+pymysql://user:password@localhost:3306/notes")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
