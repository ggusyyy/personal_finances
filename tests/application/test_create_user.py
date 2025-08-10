from dataclasses import dataclass
import pytest

from tests.mothers.create_user_dto import CreateUserDTOMother
from users.application.dtos.create_user_dto import CreateUserDTO
from users.application.use_cases.create_user_use_case import CreateUserUseCase
from users.domain.user import User
from users.domain.user_already_exists_exception import UserAlreadyExistsException
from users.domain.user_repository import UserRepository
from users.domain.value_objects.email_not_valid_exception import EmailNotValidException
from users.infrastructure.in_memory_user_repo import InMemoryUserRepository


@dataclass
class CreateUserSetup:
    repo: UserRepository
    use_case: CreateUserUseCase

@pytest.fixture
def create_user_setup() -> CreateUserSetup:
    user_repository = InMemoryUserRepository()
    use_case = CreateUserUseCase(user_repository)
    return CreateUserSetup(repo=user_repository, use_case=use_case)


def test_create_user_succesfully(create_user_setup: CreateUserSetup):
    gus: User = create_user_setup.use_case.run(
        CreateUserDTOMother.create(username="gus")
    )

    assert isinstance(gus, User)
    assert gus.username == "gus"
    assert gus.id is not None


def test_create_user_with_invalid_email(create_user_setup: CreateUserSetup):
    with pytest.raises(EmailNotValidException):
        create_user_setup.use_case.run(
            CreateUserDTOMother.create(email="invalid-email")
        )

def test_user_already_exists(create_user_setup: CreateUserSetup):
    gus: User = create_user_setup.use_case.run(
        CreateUserDTOMother.create()
    )

    with pytest.raises(UserAlreadyExistsException):
        new_gus: User = create_user_setup.use_case.run(
            CreateUserDTOMother.create(
                username=gus.username,
                email=str(gus.email),
                password=gus.password
            )
        )
