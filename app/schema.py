from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Goal 모델 정의
class GoalBase(BaseModel):
    goal: int
    goal_name: str
    description: Optional[str] = None

class GoalCreate(GoalBase):
    pass

class Goal(GoalBase):
    goal_id: int

    class Config:
        from_attributes = True


# Log 모델 정의
class LogBase(BaseModel):
    coin: int
    date: datetime = Field(default_factory=datetime.utcnow)

class LogCreate(LogBase):
    goal_id: Optional[datetime] = None

class Log(LogBase):
    id: int
    goal_id: int
    goal: Optional[Goal] = None

    class Config:
        from_attributes = True
