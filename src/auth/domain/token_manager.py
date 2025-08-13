from abc import ABC, abstractmethod

from src.auth.domain.auth_token import AuthToken


class TokenManager(ABC):
    @abstractmethod
    def encrypt_token(self, user_id: str) -> AuthToken: ...

    @abstractmethod
    def decrypt_token(self, token: AuthToken) -> str: ...