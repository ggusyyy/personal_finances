from fastapi import Depends
from src.auth.application.use_cases.login_user_use_case import LoginUserUseCase
from src.auth.domain.token_manager import TokenManager
from src.auth.infrastructure.jwt_token_manager import JwtTokenManager
from src.shared.api.deps import get_pw_hasher, get_user_repo
from src.auth.application.use_cases.register_user_use_case import RegisterUserUseCase
from src.auth.domain.pw_hasher import PasswordHasher
from src.users.domain.user_repository import UserRepository


__token_manager = JwtTokenManager()

def get_token_manager() -> TokenManager:
    return __token_manager

def get_register_user_use_case(
        repo: UserRepository = Depends(get_user_repo),
        hasher: PasswordHasher = Depends(get_pw_hasher)
    ) -> RegisterUserUseCase:
    return RegisterUserUseCase(repo, hasher)


def get_login_user_use_case(
        user_repo: UserRepository = Depends(get_user_repo),
        pw_hasher: PasswordHasher = Depends(get_pw_hasher),
        token_manager: TokenManager = Depends(get_token_manager)
    ) -> LoginUserUseCase:
    return LoginUserUseCase(user_repo, pw_hasher, token_manager)