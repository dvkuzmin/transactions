from abc import ABC, abstractmethod
from typing import Optional, List


class BalancesRepo(ABC):
    @abstractmethod
    def get_by_client_id(self, client_id: int) -> tuple:
        ...

    @abstractmethod
    def update(self, client_id: int, amount: int):
        ...


class TransactionsRepo(ABC):
    @abstractmethod
    def update(self, client_id: int):
        ...

    @abstractmethod
    def get_unresolved(self) -> Optional[List[tuple]]:
        ...

    @abstractmethod
    def get_client_by_id(self, client_id: int) -> Optional[tuple]:
        ...
