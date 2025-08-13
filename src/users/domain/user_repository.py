from abc import ABC, abstractmethod
from typing import List, Optional

from ..domain.user import User
from .value_objects.email import Email


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None: ...

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[User]: ...
    
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]: ...

    @abstractmethod
    def get_by_email(self, email: Email) -> Optional[User]: ...

    @abstractmethod
    def get_all(self) -> List[User]: ...

    @abstractmethod
    def change_password(self, new_password: str, user_id: str) -> None: ...
    
    @abstractmethod
    def delete(self, id: str) -> None: ...