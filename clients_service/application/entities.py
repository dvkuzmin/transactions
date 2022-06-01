from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Client:
    name: str
    email: str
    psw: str
    id: int = None
    date: datetime = None
    balance: Balance = None


@dataclass
class Balance:
    id: int = None
    amount: float = 0
    client: Client = None
