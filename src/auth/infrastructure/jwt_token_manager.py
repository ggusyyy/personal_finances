from datetime import datetime, timedelta
from typing import Any, MutableMapping

from dotenv import load_dotenv
from jose.exceptions import ExpiredSignatureError
from jose import JWTError, jwt
from os import environ

from src.auth.domain.auth_token import AuthToken
from src.auth.domain.exceptions.expired_token_exception import ExpiredTokenException
from src.auth.domain.exceptions.invalid_token_exception import InvalidTokenException
from src.auth.domain.token_manager import TokenManager



class JwtTokenManager(TokenManager):
    def __init__(self) -> None:
        load_dotenv()
        self.__secret_key: str = environ["JWT_SECRET_KEY"]

    def encrypt_token(self, user_id: str) -> AuthToken:
        expires_at = datetime.now() + timedelta(hours=1)
        expiration = int(expires_at.timestamp())

        payload: MutableMapping[str, Any] = {"sub": user_id, "exp": expiration}

        try:
            return AuthToken(jwt.encode(payload, self.__secret_key))
        except JWTError:
            raise InvalidTokenException()

    def decrypt_token(self, token: AuthToken) -> str:
        try:
            decoded = jwt.decode(token.content, self.__secret_key, algorithms=["HS256"])
            return decoded["sub"]
        except ExpiredSignatureError:
            raise ExpiredTokenException()
        except JWTError:
            raise InvalidTokenException()