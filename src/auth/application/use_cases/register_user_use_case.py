from datetime import datetime
from uuid import uuid4
from src.auth.domain.exceptions.email_not_valid_exception import EmailNotValidException
from src.auth.domain.exceptions.user_data_not_valid_exception import UserDataNotValidException
from src.auth.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.auth.domain.exceptions.user_passw_too_short_exception import UserPasswordTooShortException
from src.auth.application.dtos.register_user_dto import RegisterUserDTO
from src.auth.domain.pw_hasher import PasswordHasher
from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository
from src.users.domain.value_objects.email import Email
from src.auth.domain.exceptions.user_username_too_short_exception import UserUsernameTooShortException


class RegisterUserUseCase:
    def __init__(self, user_repo: UserRepository, hasher: PasswordHasher) -> None:
        self.__user_repo = user_repo
        self.__hasher = hasher
    
    def run(self, register_user_dto: RegisterUserDTO) -> User:
        if not self.__is_valid(register_user_dto):
            raise UserDataNotValidException()


        hashed_pw = self.__hasher.hash(register_user_dto.password)

        user: User = User(
            id=str(uuid4()),
            username=register_user_dto.username,
            email=Email(register_user_dto.email),
            password=hashed_pw,
            created_at=datetime.now(),
        )

        self.__user_repo.save(user)
        return user
    

    def __is_valid(self, register_user_dto: RegisterUserDTO) -> bool:
        if self.__user_repo.get_by_email(Email(register_user_dto.email)):
            raise UserAlreadyExistsException()
        
        if len(register_user_dto.password) < 6:
            raise UserPasswordTooShortException()
        
        if len(register_user_dto.username) < 3:
            raise UserUsernameTooShortException()
        
        if not Email.is_email_correct(register_user_dto.email):
            raise EmailNotValidException()
        
        return True