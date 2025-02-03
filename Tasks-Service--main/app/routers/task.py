from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.models import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.database import get_session
from app.crud import create_instance, get_instances, get_instance, update_instance, delete_instance

router = APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    new_task = Task(**task.dict())
    return create_instance(session, new_task)

@router.get("/", response_model=list[TaskResponse])
def get_tasks(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_instances(session, Task, offset, limit)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = get_instance(session, Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, session: Session = Depends(get_session)):
    task_db = get_instance(session, Task, task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_instance(session, task_db, task.dict(exclude_unset=True))

@router.delete("/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = get_instance(session, Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_instance(session, task)
    return {"message": "Task deleted successfully"}