from dataclasses import dataclass
import pytest

from src.auth.domain.auth_token import AuthToken
from src.auth.application.dtos.login_dto import LoginDTO
from src.auth.application.use_cases.login_user_use_case import LoginUserUseCase
from src.auth.domain.pw_hasher import PasswordHasher
from src.auth.domain.token_manager import TokenManager
from src.auth.infrastructure.bcrypt_pw_hasher import BcryptPasswordHasher
from src.auth.infrastructure.jwt_token_manager import JwtTokenManager
from src.users.domain.user_repository import UserRepository
from src.users.infrastructure.in_memory_user_repo import InMemoryUserRepository
from tests.mothers.user import UserMother

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


def test_login_user_successfully(login_user_setup: LoginUserSetup):
    user = UserMother.create()
    login_user_setup.repo.save(user)
    
    dto = LoginDTO(email=user.email.email, password="password123")
    user.password = login_user_setup.hasher.hash(dto.password)
    login_user_setup.repo.save(user)
    
    token: AuthToken = login_user_setup.use_case.run(dto)
    assert isinstance(token, AuthToken)

    decoded_user_id = login_user_setup.token_manager.decrypt_token(token)
    assert decoded_user_id == user.id

def test_it_raises_when_given_password_is_wrong(login_user_setup: LoginUserSetup):
    user = UserMother.create()
    login_user_setup.repo.save(user)
    user.password = login_user_setup.hasher.hash("correct-password")
    login_user_setup.repo.save(user)
    
    dto = LoginDTO(email=user.email.email, password="wrong-password")
    
    with pytest.raises(Exception):
        login_user_setup.use_case.run(dto)

def test_it_raises_when_given_email_is_not_registered(login_user_setup: LoginUserSetup):
    dto = LoginDTO(email="noone@fake.com", password="whatever")
    
    with pytest.raises(Exception):
        login_user_setup.use_case.run(dto)
