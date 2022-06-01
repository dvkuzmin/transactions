from fastapi import FastAPI
from fastapi.responses import JSONResponse
from clients.application import services, DTO
import jwt


SECRET = "DFSDDF2345msf23asdfs"


class ClientsApi(FastAPI):
    def __init__(self, clients_service: services.Clients):
        super(ClientsApi, self).__init__()
        self.clients_service = clients_service

        @self.post('/register')
        def register(client_data: DTO.ClientDTO):
            new_client = clients_service.register(client_data)
            content = {"message": f'User with {new_client.id=} was registered'}
            return JSONResponse(content=content)

        @self.post('/login')
        def login(client_data: DTO.ClientLoginDto):
            client = self.clients_service.login(client_data)
            content = {"message": f"Client with {client.id=} was succesfully logged in"}
            token = jwt.encode(
                {
                    "id": client.id,
                    "name": client.name
                },
                SECRET,
                algorithm="HS256"
            )
            headers = {"Auth-Token": token}
            return JSONResponse(content=content, headers=headers)
