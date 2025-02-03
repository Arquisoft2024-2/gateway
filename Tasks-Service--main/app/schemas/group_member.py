from sqlmodel import SQLModel

class GroupMemberBase(SQLModel):
    id_group: int
    id_member: int

class GroupMemberCreate(GroupMemberBase):
    pass

class GroupMemberRead(GroupMemberBase):
    id_group_member: int

class GroupMemberUpdate(GroupMemberBase):
    id_group: int | None = None
    id_member: int | None = None

class GroupMemberResponse(GroupMemberBase):
    id_group_member: int

    class Config:
        from_attributes = True