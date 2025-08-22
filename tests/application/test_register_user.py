from dataclasses import dataclass
import pytest

from src.auth.application.use_cases.register_user_use_case import RegisterUserUseCase
from src.auth.domain.pw_hasher import PasswordHasher
from src.auth.infrastructure.bcrypt_pw_hasher import BcryptPasswordHasher
from tests.mothers.register_user_dto import RegisterUserDTOMother
from src.users.domain.user import User
from src.auth.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.users.domain.user_repository import UserRepository
from src.auth.domain.exceptions.email_not_valid_exception import EmailNotValidException
from src.users.infrastructure.in_memory_user_repo import InMemoryUserRepository


@dataclass
class RegisterUserSetup:
    repo: UserRepository
    use_case: RegisterUserUseCase
    hasher: PasswordHasher

@pytest.fixture
def register_user_setup() -> RegisterUserSetup:
    user_repository = InMemoryUserRepository()
    hasher = BcryptPasswordHasher()
    use_case = RegisterUserUseCase(user_repository, hasher)

    return RegisterUserSetup(repo=user_repository, use_case=use_case, hasher=hasher)


def test_create_user_succesfully(register_user_setup: RegisterUserSetup):
    gus: User = register_user_setup.use_case.run(
        RegisterUserDTOMother.create(username="gus")
    )

    assert isinstance(gus, User)
    assert gus.username == "gus"
    assert gus.id is not None


def test_create_user_with_invalid_email(register_user_setup: RegisterUserSetup):
    with pytest.raises(EmailNotValidException):
        register_user_setup.use_case.run(
            RegisterUserDTOMother.create(email="invalid-email")
        )

def test_user_already_exists(register_user_setup: RegisterUserSetup):
    gus: User = register_user_setup.use_case.run(
        RegisterUserDTOMother.create()
    )

    with pytest.raises(UserAlreadyExistsException):
        register_user_setup.use_case.run(
            RegisterUserDTOMother.create(email=str(gus.email))
        )
