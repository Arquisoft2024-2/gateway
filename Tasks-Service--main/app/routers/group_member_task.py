from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.models import GroupMemberTask
from app.schemas.group_member_task import GroupMemberTaskCreate, GroupMemberTaskUpdate, GroupMemberTaskResponse
from app.database import get_session
from app.crud import create_instance, get_instances, get_instance, update_instance, delete_instance

router = APIRouter()

@router.post("/", response_model=GroupMemberTaskResponse)
def create_group_member_task(group_member_task: GroupMemberTaskCreate, session: Session = Depends(get_session)):
    new_group_member_task = GroupMemberTask(**group_member_task.dict())
    return create_instance(session, new_group_member_task)

@router.get("/", response_model=list[GroupMemberTaskResponse])
def get_group_member_tasks(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_instances(session, GroupMemberTask, offset, limit)

@router.get("/{group_member_task_id}", response_model=GroupMemberTaskResponse)
def get_group_member_task(group_member_task_id: int, session: Session = Depends(get_session)):
    group_member_task = get_instance(session, GroupMemberTask, group_member_task_id)
    if not group_member_task:
        raise HTTPException(status_code=404, detail="GroupMemberTask not found")
    return group_member_task

@router.patch("/{group_member_task_id}", response_model=GroupMemberTaskResponse)
def update_group_member_task(group_member_task_id: int, group_member_task: GroupMemberTaskUpdate, session: Session = Depends(get_session)):
    group_member_task_db = get_instance(session, GroupMemberTask, group_member_task_id)
    if not group_member_task_db:
        raise HTTPException(status_code=404, detail="GroupMemberTask not found")
    return update_instance(session, group_member_task_db, group_member_task.dict(exclude_unset=True))

@router.delete("/{group_member_task_id}")
def delete_group_member_task(group_member_task_id: int, session: Session = Depends(get_session)):
    group_member_task = get_instance(session, GroupMemberTask, group_member_task_id)
    if not group_member_task:
        raise HTTPException(status_code=404, detail="GroupMemberTask not found")
    delete_instance(session, group_member_task)
    return {"message": "GroupMemberTask deleted successfully"}