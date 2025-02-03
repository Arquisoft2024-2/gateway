from sqlmodel import SQLModel

class TaskBase(SQLModel):
    description: str
    state: str
    assignment_date: str

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id_task: int

class TaskUpdate(TaskBase):
    description: str | None = None
    state: str | None = None
    assignment_date: str | None = None

class TaskResponse(TaskBase):
    id_task: int

    class Config:
        from_attributes = True