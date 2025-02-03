from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.models import Group
from app.schemas.group import GroupCreate, GroupUpdate, GroupResponse
from app.database import get_session
from app.crud import create_instance, get_instances, get_instance, update_instance, delete_instance

router = APIRouter()

@router.post("/", response_model=GroupResponse)
def create_group(group: GroupCreate, session: Session = Depends(get_session)):
    new_group = Group(**group.dict())
    return create_instance(session, new_group)

@router.get("/", response_model=list[GroupResponse])
def get_groups(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_instances(session, Group, offset, limit)

@router.get("/{group_id}", response_model=GroupResponse)
def get_group(group_id: int, session: Session = Depends(get_session)):
    group = get_instance(session, Group, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

@router.patch("/{group_id}", response_model=GroupResponse)
def update_group(group_id: int, group: GroupUpdate, session: Session = Depends(get_session)):
    group_db = get_instance(session, Group, group_id)
    if not group_db:
        raise HTTPException(status_code=404, detail="Group not found")
    return update_instance(session, group_db, group.dict(exclude_unset=True))

@router.delete("/{group_id}")
def delete_group(group_id: int, session: Session = Depends(get_session)):
    group = get_instance(session, Group, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    delete_instance(session, group)
    return {"message": "Group deleted successfully"}
