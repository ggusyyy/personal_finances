from src.shared.api.deps import get_user_repo
from src.transactions.application.use_cases.create_transaction_use_case import CreateTransactionUseCase
from src.transactions.application.use_cases.get_transaction_use_case import GetTransactionByIdUseCase
from src.transactions.domain.transaction_repository import TransactionRepository
from src.transactions.application.use_cases.get_all_transaction_by_user_id_use_case import GetAllTransactionsByUserIdUseCase
from src.transactions.infrastructure.postgres_transaction_repository import PostgresTransactionRepository


__transaction_repo = PostgresTransactionRepository()

def get_transaction_repo() -> TransactionRepository:
    return __transaction_repo

def get_create_transaction_use_case() -> CreateTransactionUseCase:
    return CreateTransactionUseCase(__transaction_repo, get_user_repo())

def get_transaction_by_id_use_case() -> GetTransactionByIdUseCase:
    return GetTransactionByIdUseCase(__transaction_repo)

def get_all_transactions_by_user_id_use_case() -> GetAllTransactionsByUserIdUseCase:
    return GetAllTransactionsByUserIdUseCase(__transaction_repo, get_user_repo())