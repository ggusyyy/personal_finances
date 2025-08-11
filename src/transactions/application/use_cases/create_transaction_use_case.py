from datetime import datetime
from uuid import uuid4
from transactions.application.dtos.create_transaction_dto import CreateTransactionDTO
from transactions.domain.exceptions.amount_lt_zero_exception import AmountIsLessThanZeroException
from transactions.domain.transaction import Transaction
from transactions.domain.transaction_repository import TransactionRepository


class CreateTransactionUseCase:
    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def run(self, create_transaction_dto: CreateTransactionDTO) -> None:
        try:
            self.__is_valid_transaction(create_transaction_dto)
        except AmountIsLessThanZeroException as e:
            raise e
        except Exception as e:
            raise e

        transaction: Transaction = Transaction(
            id=str(uuid4()),
            user_id=create_transaction_dto.user_id,
            concept=create_transaction_dto.concept,
            kind=create_transaction_dto.kind,
            amount=create_transaction_dto.amount,
            date=datetime.now(),
        )

        self.transaction_repository.save(transaction)
    
    def __is_valid_transaction(self, transaction: CreateTransactionDTO) -> None:
        if transaction.amount <= 0:
            raise AmountIsLessThanZeroException