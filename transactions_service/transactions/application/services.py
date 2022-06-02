from dataclasses import dataclass

from .intefaces import BalancesRepo, TransactionsRepo


@dataclass
class Balances:
    balances_repo: BalancesRepo
    transactions_repo: TransactionsRepo

    def increase_balance(self, client_id: int, amount: int):
        balance = self.balances_repo.get_by_client_id(client_id)
        # client = self.transactions_repo.get_client_by_id(client_id)
        prev_balance = balance[1]
        new_balance = prev_balance + amount
        self.balances_repo.update(client_id=client_id, amount=new_balance)
        self.transactions_repo.update(client_id=client_id)
        return "balance was increased"

    def decrease_balance(self, client_id: int, amount: int):
        balance = self.balances_repo.get_by_client_id(client_id)
        # client = self.transactions_repo.get_client_by_id(client_id)
        prev_balance = balance[1]
        if prev_balance >= amount:
            new_balance = prev_balance - amount
            self.balances_repo.update(client_id=client_id, amount=new_balance)
            self.transactions_repo.update(client_id)
            return "balance was decreased"
        else:
            return "You have no enough money"

    def handle_transactions(self):
        unresolved_transactions = self.transactions_repo.get_unresolved()
        for transaction in unresolved_transactions:
            client_id = transaction[4]
            amount = transaction[3]
            method = transaction[2]
            if method == 'increase':
                self.increase_balance(client_id, amount)
            elif method == 'decrease':
                self.decrease_balance(client_id, amount)
