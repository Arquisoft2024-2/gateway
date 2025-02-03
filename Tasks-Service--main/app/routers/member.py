from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.models import Member
from app.schemas.member import MemberCreate, MemberUpdate, MemberResponse
from app.database import get_session
from app.crud import create_instance, get_instances, get_instance, update_instance, delete_instance

router = APIRouter()

@router.post("/", response_model=MemberResponse)
def create_member(member: MemberCreate, session: Session = Depends(get_session)):
    new_member = Member(**member.dict())
    return create_instance(session, new_member)

@router.get("/", response_model=list[MemberResponse])
def get_members(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_instances(session, Member, offset, limit)

@router.get("/{member_id}", response_model=MemberResponse)
def get_member(member_id: int, session: Session = Depends(get_session)):
    member = get_instance(session, Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@router.patch("/{member_id}", response_model=MemberResponse)
def update_member(member_id: int, member: MemberUpdate, session: Session = Depends(get_session)):
    member_db = get_instance(session, Member, member_id)
    if not member_db:
        raise HTTPException(status_code=404, detail="Member not found")
    return update_instance(session, member_db, member.dict(exclude_unset=True))

@router.delete("/{member_id}")
def delete_member(member_id: int, session: Session = Depends(get_session)):
    member = get_instance(session, Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    delete_instance(session, member)
    return {"message": "Member deleted successfully"}
