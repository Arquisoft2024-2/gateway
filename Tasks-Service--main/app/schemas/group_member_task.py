from sqlmodel import SQLModel

class GroupMemberTaskBase(SQLModel):
    id_task: int
    id_group_member: int

class GroupMemberTaskCreate(GroupMemberTaskBase):
    pass

class GroupMemberTaskRead(GroupMemberTaskBase):
    id_group_member_task: int

class GroupMemberTaskUpdate(GroupMemberTaskBase):
    id_task: int | None = None
    id_group_member: int | None = None

class GroupMemberTaskResponse(GroupMemberTaskBase):
    id_group_member_task: int

    class Config:
        from_attributes = True