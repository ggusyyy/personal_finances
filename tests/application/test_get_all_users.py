from dataclasses import dataclass
from typing import List

import pytest

from tests.mothers.user import UserMother
from src.users.application.use_cases.get_all_users_use_case import GetAllUsersUseCase
from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository
from src.users.infrastructure.in_memory_user_repo import InMemoryUserRepository


@dataclass
class GetAllUsersSetup:
    repo: UserRepository
    usecase: GetAllUsersUseCase

@pytest.fixture
def get_all_users_setup() -> GetAllUsersSetup:
    user_repository = InMemoryUserRepository()
    get_all_users_uc = GetAllUsersUseCase(user_repository)

    return GetAllUsersSetup(
        repo=user_repository,
        usecase=get_all_users_uc
    )

def test_all_users_are_got_succesfully(get_all_users_setup: GetAllUsersSetup):
    users: List[User] = [UserMother.create() for _ in range(5)]
    for user in users:
        get_all_users_setup.repo.save(user)

    all_users = get_all_users_setup.usecase.run()

    assert len(all_users) == 5
    for index, user in enumerate(all_users):
        assert user.id == users[index].id

def test_empty_list_is_returned_when_no_users(get_all_users_setup: GetAllUsersSetup):
    all_users = get_all_users_setup.usecase.run()

    assert len(all_users) == 0
