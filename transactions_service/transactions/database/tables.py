from sqlalchemy import Column, Integer, String, DateTime, Table, MetaData, ForeignKey, Float
from datetime import datetime

metadata = MetaData()

clients = Table(
    'clients',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False, unique=True),
    Column('psw', String, nullable=False),
    Column('date', DateTime, default=datetime.now)
)

balances = Table(
    'balances',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('amount', Float, default=0),
    Column('client_id', Integer, ForeignKey('clients.id'))
)


transactions = Table(
    'transactions',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('status', String),
    Column('method', String),
    Column('amount', Integer),
    Column('client_id', Integer, ForeignKey('clients.id')),
)
