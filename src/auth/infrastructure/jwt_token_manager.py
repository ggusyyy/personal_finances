from datetime import datetime, timedelta
from typing import Any, MutableMapping

from jose.exceptions import ExpiredSignatureError
from jose import JWTError, jwt
import os

from src.auth.domain.auth_token import AuthToken
from src.auth.domain.exceptions.expired_token_exception import ExpiredTokenException
from src.auth.domain.exceptions.invalid_token_exception import InvalidTokenException
from src.auth.domain.token_manager import TokenManager



class JwtTokenManager(TokenManager):
    def __init__(self) -> None:
        self.__secret_key: str = os.environ["JWT_SECRET_KEY"]

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
            print("decrypting")
            decoded = jwt.decode(token.content, self.__secret_key)
            print(decoded)
            print(decoded["sub"])
            return decoded["sub"]
        except ExpiredSignatureError:
            print("already expired")
            raise ExpiredTokenException()
        except JWTError as e:
            print(f"weird error: {e}")
            raise InvalidTokenException()