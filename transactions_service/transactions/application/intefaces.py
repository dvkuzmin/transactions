from abc import ABC, abstractmethod
from typing import Optional, List

from .entities import Transaction, Balance


class BalancesRepo(ABC):
    @abstractmethod
    def get_by_client_id(self, client_id: int) -> Balance:
        ...

    @abstractmethod
    def add(self, balance: Balance):
        ...


class TransactionsRepo(ABC):
    @abstractmethod
    def add(self, transaction: Transaction):
        ...

    @abstractmethod
    def get_unresolved(self) -> Optional[List[Transaction]]:
        ...
