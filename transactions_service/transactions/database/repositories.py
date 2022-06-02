from typing import Optional, List

from transactions.application import intefaces, entities
from dataclasses import dataclass
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from .tables import transactions, clients, balances


@dataclass
class BalancesRepo(intefaces.BalancesRepo):
    session: Session

    def get_by_client_id(self, client_id: int) -> entities.Balance:
        # balance = self.session.query(entities.Balance).filter(entities.Balance.client.id == client_id).one_or_none()
        selection = select(balances).where(balances.c.client_id == client_id)
        result = self.session.execute(selection).one()
        return result

    def update(self, client_id: int, amount: int):
        # try:
        #     self.session.add(balance)
        #     self.session.commit()
        # except:
        #     self.session.rollback()
        update_balance = update(balances).where(balances.c.client_id == client_id).values(amount=amount)
        self.session.execute(update_balance)
        self.session.commit()

@dataclass
class TransactionsRepo(intefaces.TransactionsRepo):
    session: Session

    def update(self, client_id: int):
        update_transaction = update(transactions).where(transactions.c.client_id == client_id).values(status='resolved')
        self.session.execute(update_transaction)
        self.session.commit()

    def get_unresolved(self) -> Optional[List[entities.Transaction]]:
        # transactions = self.session.query(entities.Transaction).filter(entities.Transaction.status == 'unresloved').all()
        selection = select(transactions).where(transactions.c.status == 'unresolved')
        result = self.session.execute(selection).all()
        print(result)
        return result

    def get_client_by_id(self, client_id: int) -> Optional[entities.Client]:
        # client = self.session.query(entities.Client).filter(entities.Client.id == client_id).one_or_none()
        selection = select(clients).where(clients.c.id == client_id)
        result = self.session.execute(selection).one()
        return result
