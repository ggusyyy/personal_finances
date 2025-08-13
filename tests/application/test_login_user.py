from dataclasses import dataclass
import pytest

from src.auth.domain.auth_token import AuthToken
from src.auth.application.dtos.login_dto import LoginDTO
from auth.application.use_cases.login_user_use_case import LoginUserUseCase
from src.auth.domain.pw_hasher import PasswordHasher
from src.auth.domain.token_manager import TokenManager
from src.auth.infrastructure.bcrypt_pw_hasher import BcryptPasswordHasher
from src.auth.infrastructure.jwt_token_manager import JwtTokenManager
from src.users.domain.user_repository import UserRepository
from src.users.infrastructure.in_memory_user_repo import InMemoryUserRepository
from tests.mothers.user import UserMother
from src.users.domain.user import User

@dataclass
class LoginUserSetup:
    repo: UserRepository
    hasher: PasswordHasher
    token_manager: TokenManager
    use_case: LoginUserUseCase

@pytest.fixture
def login_user_setup() -> LoginUserSetup:
    repo = InMemoryUserRepository()
    hasher = BcryptPasswordHasher()
    token_manager = JwtTokenManager()
    use_case = LoginUserUseCase(repo, hasher, token_manager)

    return LoginUserSetup(
        repo=repo,
        hasher=hasher,
        token_manager=token_manager,
        use_case=use_case
        )

"""
def test_login_user_successfully(login_user_setup: LoginUserSetup):
    user: User = UserMother.create()
    login_user_setup.repo.save(user)

    user_token: AuthToken = login_user_setup.use_case.run(
        LoginDTO(user.username, user.password)
    )
"""