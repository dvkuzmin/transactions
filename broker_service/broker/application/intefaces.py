from abc import ABC, abstractmethod
from typing import Optional

from .entities import Transaction


class TransactionsRepo(ABC):

    @abstractmethod
    def add(self, transaction: Transaction):
        ...

    @abstractmethod
    def change_status(self, transaction: Transaction):
        ...
