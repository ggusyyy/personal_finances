from fastapi import Depends
from src.users.application.use_cases.get_all_users_use_case import GetAllUsersUseCase
from src.users.application.use_cases.get_user_by_id_use_case import GetUserByIdUseCase
from src.users.domain.user_repository import UserRepository
from src.users.infrastructure.in_memory_user_repo import InMemoryUserRepository


__user_repo = InMemoryUserRepository()

def get_user_repo() -> UserRepository:
    return __user_repo

def get_list_all_users_use_case(
        repo: UserRepository = Depends(get_user_repo)
    ) -> GetAllUsersUseCase:
    return GetAllUsersUseCase(repo)


def get_user_by_id_use_case(
        repo: UserRepository = Depends(get_user_repo)
    ) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(repo)