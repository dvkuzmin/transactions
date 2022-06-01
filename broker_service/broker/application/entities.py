from __future__ import annotations

from dataclasses import dataclass, field
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

@dataclass
class Queue:
    id: int = field(init=False)
    client: Client = None
    transactions: list[Transaction] = field(default_factory=list)


@dataclass
class Transaction:
    id: int = field(init=False)
    status: str
    amount: int
    queue: Queue = None
