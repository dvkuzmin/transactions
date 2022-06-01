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
        try:
            self.session.add(balance)
            self.session.commit()
        except:
            self.session.rollback()


@dataclass
class TransactionsRepo(intefaces.TransactionsRepo):
    session: Session

    def add(self, transaction: entities.Transaction):
        try:
            self.session.add(transaction)
            self.session.commit()
        except:
            self.session.rollback()

    def get_unresolved(self) -> Optional[List[entities.Transaction]]:
        transactions = self.session.query(entities.Transaction).filter(entities.Transaction.status == 'unresloved').all()
        return transactions

    def get_client_by_id(self, client_id: int) -> Optional[entities.Client]:
        client = self.session.query(entities.Client).filter(entities.Client.id == client_id).one_or_none()
        return client
