from dataclasses import dataclass
from .intefaces import ClientsRepo
from .DTO import ClientDTO, ClientLoginDto
from .entities import Client, Balance
import hashlib


@dataclass
class Clients:
    clients_repo: ClientsRepo

    def register(self, client: ClientDTO):
        client.psw = hashlib.sha256(client.psw.encode()).hexdigest()
        balance = Balance()
        client = Client(name=client.name, email=client.email, psw=client.psw, balance=balance)
        self.clients_repo.add(client)
        return client

    def login(self, client_data: ClientLoginDto):
        client = self.clients_repo.get_by_email(client_data.email)
        if client:
            client_data.psw = hashlib.sha256(client_data.psw.encode()).hexdigest()
            if client.psw == client_data.psw:
                return client
            else:
                raise ValueError('password don\'t match with email')
        else:
            raise ValueError('no such email')
