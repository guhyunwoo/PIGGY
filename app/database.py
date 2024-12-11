from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import os
from dotenv import load_dotenv
import traceback
from model import Parents, Child
from base import Base

load_dotenv()
user = os.getenv("DB_USER")
host = os.getenv("DB_HOST")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}?charset=utf8"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 객체를 상속받은 모든 테이블 생성

def create_tables():
    try:
        Base.metadata.create_all(engine)
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:")
        traceback.print_exc()  # 자세한 에러 로그 출력

create_tables()