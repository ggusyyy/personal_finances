
from datetime import datetime
from enum import Enum
from faker import Faker

from src.transactions.application.dtos.create_transaction_dto import CreateTransactionDTO
from src.transactions.domain.value_objects.transaction_kind import TransactionKind

class Concept(Enum):
    PAYMENT = "payment"
    TRANSFER = "transfer"
    PURCHASE = "purchase"
    SALE = "sale"
    

class CreateTransactionDTOMother:

    faker = Faker()

    @classmethod
    def create(
        cls,
        user_id: str | None = None,
        concept: str | None = None,
        kind: TransactionKind | None = None,
        amount: float | None = None,
        date: datetime | None = None
    ) -> CreateTransactionDTO:
        user_id = user_id or cls.faker.uuid4()
        concept = concept or f"{cls.faker.random_element([concept for concept in Concept])} to {cls.faker.name()}"
        kind = kind or cls.faker.random_element([kind for kind in TransactionKind])
        amount = amount or cls.faker.random_digit_not_null()
        date = date or cls.faker.date_time()

        return CreateTransactionDTO(user_id, concept, kind, amount, date)
