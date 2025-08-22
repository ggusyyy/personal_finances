from dataclasses import dataclass
from datetime import date
from src.transactions.domain.value_objects.transaction_kind import TransactionKind

@dataclass
class CreateTransactionDTO:
    user_id: str
    concept: str
    kind: TransactionKind
    amount: float
    date: date