from src.auth.application.dtos.login_dto import LoginDTO
from src.auth.domain.auth_token import AuthToken
from src.auth.domain.exceptions.invalid_credentials_exception import InvalidCredentialsException
from src.auth.domain.pw_hasher import PasswordHasher
from src.auth.domain.token_manager import TokenManager
from src.users.domain.user_repository import UserRepository
from src.users.domain.value_objects.email import Email


class LoginUserUseCase:
    def __init__(
        self,
        user_repo: UserRepository,
        hasher: PasswordHasher,
        token_manager: TokenManager
        ) -> None:
        self.__user_repo = user_repo
        self.__hasher = hasher
        self.__token_manager = token_manager

    
    def run(self, login_dto: LoginDTO) -> AuthToken:
        user = self.__user_repo.get_by_email(Email(login_dto.email))
        if not user:
            raise InvalidCredentialsException("There is no user with this email.")
        
        hashed_pw = user.password
        
        if not self.__hasher.verify(login_dto.password, hashed_pw):
            raise InvalidCredentialsException("Invalid email or password.")
        
        return self.__token_manager.encrypt_token(user.id)