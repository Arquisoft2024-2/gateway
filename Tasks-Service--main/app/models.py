from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class Group(SQLModel, table=True):
    id_group: int = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100)
    members: int
    user_id: int
    members_list: List["GroupMember"] = Relationship(back_populates="group")


class Member(SQLModel, table=True):
    id_member: int = Field(default=None, primary_key=True)
    phone: str = Field(max_length=15)
    name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    groups: List["GroupMember"] = Relationship(back_populates="member")


class Task(SQLModel, table=True):
    id_task: int = Field(default=None, primary_key=True)
    description: str
    state: str = Field(max_length=50)
    assignment_date: str
    group_members_tasks: List["GroupMemberTask"] = Relationship(back_populates="task")


class GroupMember(SQLModel, table=True):
    id_group_member: int = Field(default=None, primary_key=True)
    id_group: int = Field(foreign_key="group.id_group")
    id_member: int = Field(foreign_key="member.id_member")
    group: Optional[Group] = Relationship(back_populates="members_list")
    member: Optional[Member] = Relationship(back_populates="groups")
    tasks: List["GroupMemberTask"] = Relationship(back_populates="group_member")


class GroupMemberTask(SQLModel, table=True):
    id_group_member_task: int = Field(default=None, primary_key=True)
    id_task: int = Field(foreign_key="task.id_task")
    id_group_member: int = Field(foreign_key="groupmember.id_group_member")
    task: Optional[Task] = Relationship(back_populates="group_members_tasks")
    group_member: Optional[GroupMember] = Relationship(back_populates="tasks")
