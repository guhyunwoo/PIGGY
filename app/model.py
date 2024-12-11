from sqlalchemy import Column, Integer, String, Float, ForeignKey
from base import Base
class Parents(Base):
    __tablename__ = "parents"

    goal_id = Column(Integer, primary_key=True, autoincrement=True)
    present_name = Column(String(255))
    goal_amount = Column(Integer, nullable=False)
    description = Column(String(1000))

    def __init__(self, present_name, goal_amount, description):
        self.present_name = present_name
        self.goal_amount = goal_amount
        self.description = description

class Child(Base):
    __tablename__ = "child"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    coin = Column(Integer, nullable=False, default=0)
    time_stamp = Column(String(20) , nullable=False)
    coin_amount = Column(Integer, nullable=False, default=0)
    progress = Column(Float, nullable=False, default=0.0)
    goal_amount = Column(Integer, nullable=False, default=0)
    goal_id = Column(Integer, ForeignKey("parents.goal_id"), nullable=False)

    def __init__(self, coin, goal_amount, time_stamp):
        self.coin_amount = 0
        self.coin = coin
        self.coin_amount += coin
        self.goal_amount = goal_amount
        self.progress = float(self.coin_amount / self.goal_amount) * 100
        self.time_stamp = time_stamp