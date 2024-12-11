from pydantic import BaseModel

class ChildBase(BaseModel):
    log_id: int
    coin: int
    time_stamp: str
    coin_amount: int
    progress: float

class ParentsBase(BaseModel):
    goal_id: int
    present_name: str
    goal_amount: int
    description: str

class ChildCreate(ChildBase):
    pass

class ParentsCreate(ParentsBase):
    pass

class Child(ChildBase):
    id: int
    class Config:
        from_attributes = True

class Parents(ParentsBase):
    id: int
    class Config:
        from_attributes = True
