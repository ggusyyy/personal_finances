from datetime import date
from pydantic import BaseModel

from src.transactions.domain.value_objects.transaction_kind import TransactionKind


class TransactionCreate(BaseModel):
    concept: str
    kind: TransactionKind
    amount: float
    date: date
    
class TransactionOut(BaseModel):
    id: str
    concept: str
    kind: TransactionKind
    amount: float
    date: date