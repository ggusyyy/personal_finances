from abc import ABC, abstractmethod
from typing import List, Optional

from src.transactions.domain.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> None: ...

    @abstractmethod
    def get_by_id(self, transaction_id: str) -> Optional[Transaction]: ...

    @abstractmethod
    def get_all_by_user_id(self, user_id: str) -> List[Transaction]: ...