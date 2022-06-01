from typing import Optional, List

from transactions.application import intefaces, entities
from dataclasses import dataclass
from sqlalchemy.orm import Session


@dataclass
class BalancesRepo(intefaces.BalancesRepo):
    session: Session

    def get_by_client_id(self, client_id: int) -> entities.Balance:
        balance = self.session.query(entities.Balance).filter(entities.Balance.client.id == client_id).one_or_none()
        return balance

    def add(self, balance: entities.Balance):
        self.session.add(balance)
        self.session.commit()


@dataclass
class TransactionsRepo(intefaces.TransactionsRepo):
    session: Session

    def add(self, transaction: entities.Transaction):
        self.session.add(transaction)
        self.session.commit()

    def get_unresolved(self) -> Optional[List[entities.Transaction]]:
        transactions = self.session.query(entities.Transaction).filter(entities.Transaction.status == 'await').all()
        return transactions
