from fastapi import FastAPI
from transactions.application import services


class ClientsApi(FastAPI):
    def __init__(self, balances_service: services.Balances):
        super(ClientsApi, self).__init__()
        self.balances_service = balances_service

        @self.get('/increase')
        def increase(client_id: int, amount: int):
            self.balances_service.increase_balance(client_id, amount)

        @self.get('/decrease')
        def decrease(client_id: int, amount: int):
            self.balances_service.decrease_balance(client_id, amount)
