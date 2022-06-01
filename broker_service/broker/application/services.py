from dataclasses import dataclass
from .intefaces import TransactionsRepo
from .DTO import ClientDTO, ClientLoginDto
from .entities import Client, Balance


@dataclass
class Transactions:
    transactions_repo: TransactionsRepo

    def create_queue(self, email: str):
        pass

    def change_balance(self, method: str, amount: int):
        pass
