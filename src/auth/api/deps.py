from fastapi import Depends
from src.shared.api.deps import get_pw_hasher, get_user_repo
from src.auth.application.use_cases.register_user_use_case import RegisterUserUseCase
from src.auth.domain.pw_hasher import PasswordHasher
from src.users.domain.user_repository import UserRepository



def get_register_user_use_case(
        repo: UserRepository = Depends(get_user_repo),
        hasher: PasswordHasher = Depends(get_pw_hasher)
    ) -> RegisterUserUseCase:
    return RegisterUserUseCase(repo, hasher)