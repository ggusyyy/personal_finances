from dataclasses import dataclass

import pytest

from tests.mothers.transaction_dto import CreateTransactionDTOMother
from src.transactions.application.use_cases.create_transaction_use_case import CreateTransactionUseCase
from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository
from src.transactions.infrastructure.in_memory_transaction_repository import InMemoryTransactionRepository
from src.transactions.domain.exceptions.amount_lt_zero_exception import AmountIsLessThanZeroException
from src.users.domain.user_repository import UserRepository
from src.users.infrastructure.in_memory_user_repo import InMemoryUserRepository
from tests.mothers.user import UserMother
from src.users.domain.user import User


@dataclass
class CreateTransactionSetup:
    transaction_repo: TransactionRepository
    user_repo: UserRepository
    use_case: CreateTransactionUseCase

@pytest.fixture
def create_transaction_setup() -> CreateTransactionSetup:
    transaction_repository = InMemoryTransactionRepository()
    user_repository = InMemoryUserRepository()
    use_case = CreateTransactionUseCase(transaction_repository, user_repository)
    
    return CreateTransactionSetup(transaction_repository, user_repository, use_case)

def test_create_transaction_succesfully(create_transaction_setup: CreateTransactionSetup):
    
    user: User = UserMother.create()
    create_transaction_setup.user_repo.save(user)
    
    
    transaction: Transaction = create_transaction_setup.use_case.run(
        CreateTransactionDTOMother.create(user_id=user.id)
    )
    
    assert isinstance(transaction, Transaction)
    assert transaction.id is not None
    assert transaction.user_id is not None

def test_it_raises_when_transaction_amount_is_lt_zero(create_transaction_setup: CreateTransactionSetup):
    with pytest.raises(AmountIsLessThanZeroException):
        create_transaction_setup.use_case.run(
            CreateTransactionDTOMother.create(
                amount=-2
            )
        )