from typing import Optional

from application import intefaces, entities
from dataclasses import dataclass
from sqlalchemy.orm import Session


@dataclass
class ClientsRepo(intefaces.ClientsRepo):
    session: Session

    def add(self, client: entities.Client):
        self.session.add(client)
        self.session.commit()

    def get_by_email(self, email: str) -> Optional[entities.Client]:
        client = self.session.query(entities.Client).filter(entities.Client.email == email).one_or_none()
        return client

    def get_by_id(self, client_id: int) -> Optional[entities.Client]:
        pass
