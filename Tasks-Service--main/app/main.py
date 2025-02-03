from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import group, member, task, group_member, group_member_task
from strawberry.fastapi import GraphQLRouter
import strawberry


app = FastAPI(docs_url="/docs", redoc_url=None, openapi_url="/openapi.json")

@strawberry.type
class Query:
    hello: str = "Hello from FastAPI GraphQL!"



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "coneccion completada con task service"}

schema = strawberry.Schema(Query)
graphql_router = GraphQLRouter(schema)

app.include_router(graphql_router, prefix="/graphql")
app.include_router(group.router, prefix="/group", tags=["groups"])
app.include_router(member.router, prefix="/member", tags=["members"])
app.include_router(task.router, prefix="/task", tags=["tasks"])
app.include_router(group_member.router, prefix="/group_member", tags=["group_members"])
app.include_router(group_member_task.router, prefix="/group_member_task", tags=["group_member_tasks"])
