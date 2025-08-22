from src.transactions.domain.exceptions.transaction_not_found_exception import TransactionNotFoundException
from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository


class GetTransactionByIdUseCase:
    def __init__(self, transaction_repository: TransactionRepository) -> None:
        self.repo = transaction_repository
        
    def run(self, transaction_id: str) -> Transaction:
        transaction = self.repo.get_by_id(transaction_id)
        
        if not transaction:
            raise TransactionNotFoundException
        
        return transaction