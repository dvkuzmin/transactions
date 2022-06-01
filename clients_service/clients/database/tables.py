from sqlalchemy import Column, Integer, String, DateTime, Table, MetaData, ForeignKey, Float
from datetime import datetime

metadata = MetaData()

clients = Table(
    'transactions',
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
    Column('client_id', Integer, ForeignKey('transactions.id'))
)

queues = Table(
    'queues',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('client_id', Integer, ForeignKey('transactions.id')),
)

transactions = Table(
    'transactions',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('status', String),
    Column('amount', Integer),
    Column('queue_id', Integer, ForeignKey('queues.id')),
)
