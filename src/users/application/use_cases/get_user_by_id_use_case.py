from src.users.api.schemas import UserOut
from src.users.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.users.domain.user_repository import UserRepository


class GetUserByIdUseCase:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def run(self, id: str) -> UserOut:
        user = self.user_repository.get_by_id(id)
        if not user:
            raise UserNotFoundException()
        
        return UserOut(
            id=user.id,
            username=user.username,
            email=str(user.email),
        )