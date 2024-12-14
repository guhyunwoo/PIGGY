from typing import Any
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.sql import func

class Goal(Base):
    __tablename__ = "goal"

    goal_id = Column(Integer, primary_key=True, autoincrement=True)
    goal_value = Column(Integer, nullable=False)
    goal_name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=True)
    log = relationship("Log", back_populates="goal")

class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(Integer, nullable=False, default=0)
    date = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    goal_id = Column(Integer, ForeignKey('goal.goal_id'))  # 외래 키(ForeignKey) 추가
    goal = relationship("Goal", back_populates="log")  # 관계 설정