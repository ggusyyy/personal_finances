from datetime import datetime
from uuid import uuid4
from src.users.application.dtos.create_user_dto import CreateUserDTO
from src.users.domain.user import User
from src.users.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.users.domain.exceptions.user_data_not_valid_exception import UserNotValidException
from src.users.domain.exceptions.user_passw_too_short_exception import UserPasswordTooShortException
from src.users.domain.user_repository import UserRepository
from src.users.domain.exceptions.user_username_too_short_exception import UserUsernameTooShortException
from src.users.domain.value_objects.email import Email
from src.users.domain.value_objects.email_not_valid_exception import EmailNotValidException


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def run(self, input: CreateUserDTO) -> User:
        if not self.__is_valid(input):
            raise UserNotValidException

        if self.user_repository.get_by_email(Email(input.email)):
            raise UserAlreadyExistsException

        user: User = User(
            id=str(uuid4()),
            username=input.username,
            email=Email(input.email),
            password=input.password,
            created_at=datetime.now()
        )
        self.user_repository.save(user)
        return user

    def __is_valid(self, user_data: CreateUserDTO) -> bool:
        if not Email.is_email_correct(user_data.email):
            raise EmailNotValidException
        if len(user_data.username) < 3:
            raise UserUsernameTooShortException
        if len(user_data.password) < 6:
            raise UserPasswordTooShortException

        return True