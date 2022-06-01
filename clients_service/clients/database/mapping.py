from clients.application import entities
from sqlalchemy.orm import registry, relationship

from .tables import clients, balances, transactions

mapper = registry()

mapper.map_imperatively(
    entities.Balance,
    balances
)

mapper.map_imperatively(
    entities.Transaction,
    transactions
)

mapper.map_imperatively(
    entities.Client,
    clients,
    properties={
        'balance':  relationship(entities.Balance, backref='client', uselist=False),
        'transactions':  relationship(entities.Transaction, backref='client', uselist=True)
    }
)
