from dataclasses import dataclass
from .intefaces import BalancesRepo, TransactionsRepo


@dataclass
class Balances:
    balances_repo: BalancesRepo
    transactions_repo: TransactionsRepo

    def increase_balance(self, client_id: int, amount: int):
        balance = self.balances_repo.get_by_client_id(client_id)
        balance.amount += amount
        self.balances_repo.add(balance)
        return "balance was increased"

    def decrease_balance(self, client_id: int, amount: int):
        balance = self.balances_repo.get_by_client_id(client_id)
        if balance.amount >= amount:
            balance.amount -= amount
            return "balance was decreased"
        else:
            return "You have no enough money"

    def handle_transactions(self):
        unresolved_transactions = self.transactions_repo.get_unresolved()
        for transaction in unresolved_transactions:
            client_id = transaction.queue.client.id
            amount = transaction.amount
            method = transaction.method
            if method == 'increase':
                self.increase_balance(client_id, amount)
            elif method == 'decrease':
                self.decrease_balance(client_id, amount)
