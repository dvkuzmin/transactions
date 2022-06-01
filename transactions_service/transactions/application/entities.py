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
    queue: Queue = None


@dataclass
class Balance:
    id: int = field(init=False)
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
    method: str
    status: str
    amount: int
    queue: Queue = None
