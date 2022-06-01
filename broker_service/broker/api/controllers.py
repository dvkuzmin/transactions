from fastapi import FastAPI
from fastapi.responses import JSONResponse


class ClientsApi(FastAPI):
    def __init__(self):
        super(ClientsApi, self).__init__()

        @self.get('/createQueue')
        def create_queue(email: str):
            pass

        @self.get('/changeBalance')
        def change_balance(method: str, amount: int):
            pass
