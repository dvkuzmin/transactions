from clients.application import entities
from sqlalchemy.orm import registry, relationship

from .tables import clients, balances, queues, transactions

mapper = registry()

mapper.map_imperatively(
    entities.Balance,
    balances
)

mapper.map_imperatively(
    entities.Queue,
    queues
)

mapper.map_imperatively(
    entities.Client,
    clients,
    properties={
        'balance':  relationship(entities.Balance, backref='client', uselist=False),
        'queue':  relationship(entities.Queue, backref='client', uselist=False)
    }
)

mapper.map_imperatively(
    entities.Transaction,
    transactions,
    properties={
        'queue': relationship(entities.Queue, backref='transactions', uselist=True)
    }
)
