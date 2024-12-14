from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database import SessionLocal
from datetime import datetime, timedelta
from . import model, schema

def get_logs(db: Session):
    return db.query(model.Log).order_by(model.Log.date.desc()).all()

def get_weekly_amount(db: Session):
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

def create_log(db: Session, log: schema.LogCreate):
    db_log = model.Log(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
