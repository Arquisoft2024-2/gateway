from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.models import GroupMember
from app.schemas.group_member import GroupMemberCreate, GroupMemberUpdate, GroupMemberResponse
from app.database import get_session
from app.crud import create_instance, get_instances, get_instance, update_instance, delete_instance

router = APIRouter()

@router.post("/", response_model=GroupMemberResponse)
def create_group_member(group_member: GroupMemberCreate, session: Session = Depends(get_session)):
    new_group_member = GroupMember(**group_member.dict())
    return create_instance(session, new_group_member)

@router.get("/", response_model=list[GroupMemberResponse])
def get_group_members(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_instances(session, GroupMember, offset, limit)

@router.get("/{group_member_id}", response_model=GroupMemberResponse)
def get_group_member(group_member_id: int, session: Session = Depends(get_session)):
    group_member = get_instance(session, GroupMember, group_member_id)
    if not group_member:
        raise HTTPException(status_code=404, detail="GroupMember not found")
    return group_member

@router.patch("/{group_member_id}", response_model=GroupMemberResponse)
def update_group_member(group_member_id: int, group_member: GroupMemberUpdate, session: Session = Depends(get_session)):
    group_member_db = get_instance(session, GroupMember, group_member_id)
    if not group_member_db:
        raise HTTPException(status_code=404, detail="GroupMember not found")
    return update_instance(session, group_member_db, group_member.dict(exclude_unset=True))

@router.delete("/{group_member_id}")
def delete_group_member(group_member_id: int, session: Session = Depends(get_session)):
    group_member = get_instance(session, GroupMember, group_member_id)
    if not group_member:
        raise HTTPException(status_code=404, detail="GroupMember not found")
    delete_instance(session, group_member)
    return {"message": "GroupMember deleted successfully"}
