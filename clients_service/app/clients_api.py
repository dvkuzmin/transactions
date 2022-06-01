from sqlalchemy import create_engine

import database
import api
from application import services


class Settings:
    db = database.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)
    session_local = database.SessionLocal(engine)
    clients_repo = database.repositories.ClientsRepo(session_local.session)


class Application:
    clients = services.Clients(clients_repo=DB.clients_repo)


app = api.ClientsApi(Application.clients)
