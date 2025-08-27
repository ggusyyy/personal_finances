import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from src.transactions.api.deps import get_all_transactions_by_user_id_use_case, get_create_transaction_use_case, get_transaction_by_id_use_case
from src.transactions.api.schemas import TransactionCreate, TransactionOut
from src.transactions.application.dtos.create_transaction_dto import CreateTransactionDTO
from src.transactions.application.use_cases.create_transaction_use_case import CreateTransactionUseCase
from src.transactions.application.use_cases.get_transaction_use_case import GetTransactionByIdUseCase
from src.transactions.domain.transaction import Transaction
from src.transactions.application.use_cases.get_all_transaction_by_user_id_use_case import GetAllTransactionsByUserIdUseCase


router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/transactions", response_model=TransactionOut, status_code=status.HTTP_201_CREATED)
def create_transaction(
    new_transaction: TransactionCreate,
    user_id: str,
    create_transaction_use_case: CreateTransactionUseCase = Depends(get_create_transaction_use_case),
) -> TransactionOut:
    """
    Endpoint to create a new transaction
    """
    
    try:
        transaction: Transaction = create_transaction_use_case.run(
            CreateTransactionDTO(
                user_id=user_id,
                concept=new_transaction.concept,
                kind=new_transaction.kind,
                amount=new_transaction.amount,
                date=new_transaction.date
            )
        )
    
    except Exception as e:
        logging.error(f"Error creating transaction: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error creating transaction"
        )
    
    return TransactionOut(
        id=transaction.id,
        concept=transaction.concept,
        kind=transaction.kind,
        amount=transaction.amount,
        date=transaction.date
    )
    
@router.get("/transactons", response_model=TransactionOut)
def get_transaction(
    transaction_id: str,
    use_case: GetTransactionByIdUseCase = Depends(get_transaction_by_id_use_case)
):
    """
    Endpoint to get a transaction by id
    """
    
    try:
        transaction: Transaction = use_case.run(transaction_id)
    except Exception as e:
        logging.error(f"Error getting transaction: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error getting transaction"
        )
        
    return TransactionOut(
        id=transaction.id,
        concept=transaction.concept,
        kind=transaction.kind,
        amount=transaction.amount,
        date=transaction.date
    )
    
@router.get("/transactions", response_model=List[TransactionOut])
def get_all_transactions_by_user_id(
    user_id: str,
    use_case: GetAllTransactionsByUserIdUseCase = Depends(get_all_transactions_by_user_id_use_case)
):
    """
    Endpoint to get all transactions by user id
    """
    
    try:
        transactions: List[Transaction] = use_case.run(user_id)
    except Exception as e:
        logging.error(f"Error getting transaction: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error getting transaction"
        )
        
    return [
        TransactionOut(
            id=transaction.id,
            concept=transaction.concept,
            kind=transaction.kind,
            amount=transaction.amount,
            date=transaction.date
        ) for transaction in transactions
    ]