import pytest

from dataclasses import dataclass

from tests.mothers.user import UserMother
from users.api.schemas import UserOut
from users.application.use_cases.get_user_by_id_use_case import GetUserByIdUseCase
from users.domain.user import User
from users.domain.user_not_found_exception import UserNotFoundException
from users.domain.user_repository import UserRepository
from users.infrastructure.in_memory_user_repo import InMemoryUserRepository


@dataclass
class GetUserByIdSetup:
    repo: UserRepository
    usecase: GetUserByIdUseCase


@pytest.fixture
def get_user_by_id_setup() -> GetUserByIdSetup:
    user_repository = InMemoryUserRepository()
    get_user_by_id_uc = GetUserByIdUseCase(user_repository)

    return GetUserByIdSetup(
        repo=user_repository,
        usecase=get_user_by_id_uc
        )


def test_user_is_got_succesfully(get_user_by_id_setup: GetUserByIdSetup):
    gus: User = UserMother.create()
    get_user_by_id_setup.repo.save(gus)

    new_gus: UserOut = get_user_by_id_setup.usecase.run(gus.id)

    assert new_gus is not None
    assert new_gus.id == gus.id
    assert new_gus.username == gus.username


def test_it_raises_when_user_not_found(get_user_by_id_setup: GetUserByIdSetup):
    with pytest.raises(UserNotFoundException):
        get_user_by_id_setup.usecase.run("non-existent-id")
