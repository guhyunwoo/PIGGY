from fastapi import FastAPI
from fastapi.params import Depends, Body
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import model, schema, database
from datetime import datetime, timedelta

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def get_all():
    return {"message": "Welcome to the API!"}

@app.get("/log")
def get_log_all(db: Session = Depends(get_db)):
    return db.query(model.Log).order_by(model.Log.date.desc()).all()

@app.get("/log/weekly")
def get_weekly_amount(db: Session = Depends(get_db)):
    # 현재 날짜와 시간 가져오기
    now = datetime.now()

    # 이번 주 일요일 0시 계산
    monday_start = now - timedelta(days=now.weekday())
    monday_start = monday_start.replace(hour=0, minute=0, second=0, microsecond=0)

    # 이번 주 일요일 이후의 로그만 가져오기
    return (
        db.query(func.sum(model.Log.coin))
        .filter(model.Log.date >= monday_start)  # 일요일 이후의 로그
        .scalar() or 0  # 결과 가져오기
    )

@app.post("/log")
def create_log(db: Session = Depends(get_db), log: schema.LogCreate = Body(...)):
    db_log = model.Log(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log