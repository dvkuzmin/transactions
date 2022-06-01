from abc import ABC, abstractmethod
from typing import Optional

from .entities import Client, Transaction


class ClientsRepo(ABC):

    @abstractmethod
    def get_by_id(self, client_id: int) -> Optional[Client]:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[Client]:
        ...

    @abstractmethod
    def add(self, client: Client):
        ...

    @abstractmethod
    def add_transaction(self, transaction: Transaction):
        ...
