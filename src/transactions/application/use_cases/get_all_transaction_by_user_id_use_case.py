from typing import List, Optional

from src.transactions.domain.transaction import Transaction
from src.transactions.domain.transaction_repository import TransactionRepository
from src.users.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository


class GetAllTransactionsByUserIdUseCase:
    def __init__(
        self,
        transaction_repo: TransactionRepository,
        user_repo: UserRepository
        ) -> None:
        self.__transaction_repo = transaction_repo
        self.__user_repo = user_repo
    
    def run(self, user_id: str):
        user: Optional[User] = self.__user_repo.get_by_id(user_id)
        
        if not user:
            raise UserNotFoundException()
        
        
        transactions: List[Transaction] = self.__transaction_repo.get_all_by_user_id(user_id)
        
        return transactions