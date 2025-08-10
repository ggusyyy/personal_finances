from typing import List
from users.api.schemas import UserOut
from users.domain.user import User
from users.domain.user_repository import UserRepository


class GetAllUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def run(self) -> List[UserOut]:
        users: List[User] = self.user_repository.get_all()
        return [
            UserOut(
                id=user.id,
                username=user.username,
                email=str(user.email)
            )
            for user in users
        ]