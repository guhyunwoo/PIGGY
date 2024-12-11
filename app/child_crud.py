from sqlalchemy.orm import Session
from app.model import Child
from app.schema import ChildCreate

def get_child(db: Session):
    return db.query(Child).all()

def get_one_child(db: Session, log_id: int):
    return db.query(Child).filter(Child.log_id == log_id).first()

def create_child(db: Session, child: ChildCreate):
    db_child = Child(**child.dict())
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child

def update_child(db: Session, child: Child, updated_child: ChildCreate):
    for key, value in updated_child.dict().items():
        setattr(child, key, value)
    db.commit()
    db.refresh(child)
    return child

def delete_child(db: Session, child: Child):
    db.delete(child)
    db.commit()

