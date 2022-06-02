from sqlalchemy.orm import sessionmaker
import os
from pydantic import BaseSettings


user = os.getenv('DB_USER', 'test_user')
password = os.getenv('DB_PASSWORD', 'mysecretpassword')
host = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '5432')
database = os.getenv('DB_DATABASE', 'test_db')


class Settings(BaseSettings):
    DB_URL: str = f"postgresql+psycopg2://{user}:" \
          f"{password}@{host}:{port}/{database}"


class SessionLocal:
    def __init__(self, engine):
        self.create_session = sessionmaker(engine)

    @property
    def session(self):
        return self.create_session()
