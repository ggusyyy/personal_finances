from transactions.domain.value_objects.transaction_kind import TransactionKind


class CreateTransactionDTO:
    user_id: str
    concept: str
    kind: TransactionKind
    amount: float