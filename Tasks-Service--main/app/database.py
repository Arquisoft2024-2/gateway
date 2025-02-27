import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session

load_dotenv()

db_username = os.getenv('USER_DB')
db_password = os.getenv("PASSWORD_DB")
db_host = os.getenv("HOST_DB")
db_name = os.getenv("NAME_DB")

url_connection = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:28309/{db_name}'
engine = create_engine(url_connection)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
