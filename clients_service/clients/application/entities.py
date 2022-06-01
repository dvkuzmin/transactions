from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Client:
    id: int = field(init=False)
    name: str
    email: str
    psw: str
    date: datetime = None
    balance: Balance = None
    transactions: list[Transaction] = field(default_factory=list)


@dataclass
class Balance:
    id: int = field(init=False)
    amount: float = 0
    client: Client = None


@dataclass
class Transaction:
    id: int = field(init=False)
    status: str = None
    amount: int = None
    method: str = None
    client: Client = None
