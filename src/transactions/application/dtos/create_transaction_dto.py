from dataclasses import dataclass
from datetime import date

@dataclass
class CreateTransactionDTO:
    user_id: str
    concept: str
    kind: str
    amount: float
    date: date