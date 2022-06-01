from sqlalchemy import create_engine

from transactions import database
from transactions import api
from transactions.application import services


class Settings:
    db = database.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    session_local = database.SessionLocal(engine)
    balances_repo = database.repositories.BalancesRepo(session_local.session)
    transactions_repo = database.repositories.TransactionsRepo(session_local.session)


class Application:
    balances = services.Balances(
        balances_repo=DB.balances_repo,
        transactions_repo=DB.transactions_repo
    )


app = api.ClientsApi(Application.balances)
