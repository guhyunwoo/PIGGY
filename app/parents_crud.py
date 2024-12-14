from sqlalchemy.orm import Session
from . import model, schema

def get_goals(db: Session):
    return db.query(model.Goal).order_by(model.Goal.goal_id.desc()).all()

def create_goal(db: Session, goal: schema.GoalCreate):
    db_goal = model.Goal(**goal.model_dump())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
