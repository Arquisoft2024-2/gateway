from sqlmodel import SQLModel

class MemberBase(SQLModel):
    phone: str
    name: str
    last_name: str

class MemberCreate(MemberBase):
    pass

class MemberRead(MemberBase):
    id_member: int

class MemberUpdate(MemberBase):
    phone: str | None = None
    name: str | None = None
    last_name: str | None = None

class MemberResponse(MemberBase):
    id_member: int

    class Config:
        from_attributes = True