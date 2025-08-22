from datetime import datetime
from faker import Faker

from src.transactions.domain.transaction import Transaction
from src.transactions.domain.value_objects.transaction_kind import TransactionKind


class TransactionMother:
    faker = Faker()
    
    @classmethod
    def create(
        cls, 
        id: str | None = None,
        user_id: str | None = None,
        concept: str | None = None,
        kind: TransactionKind | None = None,
        amount: float | None = None,
        date: datetime | None = None
    ) -> Transaction:
        id = id or cls.faker.uuid4()
        user_id = user_id or cls.faker.user_name()
        concept = concept or cls.faker.email()
        kind = kind or cls.faker.random_element([kind for kind in TransactionKind])
        amount = amount or cls.faker.random_digit_not_null()
        date = date or cls.faker.date_time()
        
        return Transaction(id, user_id, concept, kind, amount, date)