from src.auth.domain.pw_hasher import PasswordHasher
from src.auth.infrastructure.bcrypt_pw_hasher import BcryptPasswordHasher
from src.users.domain.user_repository import UserRepository
from src.users.infrastructure.postgres_user_repository import PostgresUserRepository


__user_repo = PostgresUserRepository()
__pw_hasher = BcryptPasswordHasher()

def get_user_repo() -> UserRepository:
    return __user_repo

def get_pw_hasher() -> PasswordHasher:
    return __pw_hasher