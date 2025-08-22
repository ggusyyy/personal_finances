from dataclasses import dataclass
from typing import Optional

import pytest

from tests.mothers.transaction import TransactionMother
from src.transactions.application.use_cases.get_transaction_use_case import GetTransactionByIdUseCase
from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository
from src.transactions.infrastructure.in_memory_transaction_repository import InMemoryTransactionRepository


@dataclass
class GetTransactionByIdSetup:
    repo: TransactionRepository
    use_case: GetTransactionByIdUseCase

@pytest.fixture
def get_transaction_by_id_setup() -> GetTransactionByIdSetup:
    repo = InMemoryTransactionRepository()
    use_case = GetTransactionByIdUseCase(repo)
    
    return GetTransactionByIdSetup(repo, use_case)

def test_transaction_is_got_succesfully(get_transaction_by_id_setup: GetTransactionByIdSetup):
    transaction = TransactionMother.create()
    get_transaction_by_id_setup.repo.save(transaction)
    
    new_transaction: Optional[Transaction] = get_transaction_by_id_setup.repo.get_by_id(
        transaction.id
    )
    
    assert new_transaction is not None
    assert new_transaction.id == transaction.id