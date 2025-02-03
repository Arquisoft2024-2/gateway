from sqlmodel import SQLModel

class GroupBase(SQLModel):
    nombre: str
    members: int
    user_id: int

class GroupCreate(GroupBase):
    pass

class GroupRead(GroupBase):
    id_group: int

class GroupUpdate(GroupBase):
    nombre: str | None = None
    members: int | None = None
    user_id: int | None = None

class GroupResponse(GroupBase):
    id_group: int

    class Config:
        from_attributes = True