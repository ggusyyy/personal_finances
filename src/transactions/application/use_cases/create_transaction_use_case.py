from typing import Optional
from uuid import uuid4

from src.transactions.application.dtos.create_transaction_dto import CreateTransactionDTO
from src.transactions.domain.exceptions.amount_lt_zero_exception import AmountIsLessThanZeroException
from src.transactions.domain.exceptions.transaction_data_not_valid_exception import TransactionDataIsNotValidException
from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository
from src.transactions.domain.value_objects.transaction_kind import TransactionKind
from src.users.domain.user_repository import UserRepository
from src.transactions.domain.exceptions.transaction_kind_not_valid_exception import TransactionKindIsNotValidException
from src.users.domain.user import User
from src.transactions.domain.exceptions.transaction_user_id_not_valid_exception import TransactionUserIdIsNotValidException


class CreateTransactionUseCase:
    def __init__(
        self,
        transaction_repository: TransactionRepository,
        user_repository: UserRepository
        ):
        self.__transaction_repository = transaction_repository
        self.__user_repository = user_repository

    def run(self, create_transaction_dto: CreateTransactionDTO) -> Transaction:
        if not self.__is_valid_transaction(create_transaction_dto):
            raise TransactionDataIsNotValidException

        transaction: Transaction = Transaction(
            id=str(uuid4()),
            user_id=create_transaction_dto.user_id,
            concept=create_transaction_dto.concept,
            kind=create_transaction_dto.kind,
            amount=create_transaction_dto.amount,
            date=create_transaction_dto.date,
        )

        self.__transaction_repository.save(transaction)
        
        return transaction
    
    def __is_valid_transaction(self, transaction: CreateTransactionDTO) -> bool:
        if transaction.amount <= 0:
            raise AmountIsLessThanZeroException
        
        if transaction.kind not in TransactionKind:
            raise TransactionKindIsNotValidException
        
        user: Optional[User] = self.__user_repository.get_by_id(transaction.user_id)
        if not user:
            raise TransactionUserIdIsNotValidException
        
        
        return True