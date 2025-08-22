from typing import Dict

from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository

class InMemoryTransactionRepository(TransactionRepository):
    def __init__(self):
        self.transactions: Dict[str, Transaction] = {}

    def save(self, transaction: Transaction) -> None:
        self.transactions[transaction.id] = transaction

    def get_by_id(self, transaction_id: str):
        return self.transactions.get(transaction_id)

    def get_all_by_user_id(self, user_id: str):
        return [
            transaction
            for transaction
            in self.transactions.values()
            if transaction.user_id == user_id
            ]