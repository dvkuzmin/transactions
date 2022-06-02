import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from clients.application import services, DTO
import jwt


SECRET = "DFSDDF2345msf23asdfs"


class ClientsApi(FastAPI):
    def __init__(self, clients_service: services.Clients):
        super(ClientsApi, self).__init__()
        self.clients_service = clients_service

        def _auth(request: Request):
            if 'Authorization' in request.headers:
                method, token = request.headers['Authorization'].split()
                if method in ('Bearer', 'JWT'):
                    data = jwt.decode(token, SECRET, algorithms=['HS256'])
                    if data['email']:
                        client = self.clients_service.get_by_email(data['email'])
                        if client:
                            return client
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError

        @self.post('/register')
        def register(client_data: DTO.ClientDTO):
            new_client = clients_service.register(client_data)
            content = {"message": f'User with {new_client.id=} was registered!'}
            return JSONResponse(content=content)

        @self.post('/login')
        def login(client_data: DTO.ClientLoginDto):
            client = self.clients_service.login(client_data)
            content = {"message": f"Client with {client.id=} was successfully logged in"}
            token = jwt.encode(
                {
                    "email": client.email
                },
                SECRET,
                algorithm="HS256"
            )
            headers = {"Auth-Token": token}
            return JSONResponse(content=content, headers=headers)

        @self.get('/increase')
        def increase(amount: int, request: Request):
            client = _auth(request)
            params = {'amount': amount, 'client_id': client.id}
            try:
                # requests.get("http://transaction_service:8001/increase", params=params)
                requests.get("http://localhost:8001/increase", params=params)
                return JSONResponse(content="Your balance was increased")
            except:
                self.clients_service.add_unresolved_transaction(
                    client_id=client.id,
                    amount=amount,
                    method='increase'
                )
                return JSONResponse(content="Service is not available, your transactions has been saved")

        @self.get('/decrease')
        def decrease(amount: int, request: Request):
            client = _auth(request)
            params = {'amount': amount, 'client_id': client.id}
            try:
                # requests.get("http://transaction_service:8001/decrease", params=params)
                requests.get("http://localhost:8001/decrease", params=params)
                return JSONResponse(content="Your balance was increased")
            except:
                self.clients_service.add_unresolved_transaction(
                    client_id=client.id,
                    amount=amount,
                    method='decrease'
                )
                return JSONResponse(content="Service is not available, your transactions has been saved")
