from typing import Dict, List, Optional
from src.users.domain.user import User
from src.users.domain.user_repository import UserRepository
from src.users.domain.value_objects.email import Email


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: Dict[str, User] = {}

    def save(self, user: User) -> None:
        self.users[user.id] = user
    
    def get_by_id(self, id: str) -> Optional[User]:
        for user in self.users.values():
            if user.id == id:
                return user     
        return None
    
    def get_by_email(self, email: Email) -> Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None
    
    def get_all(self) -> List[User]:
        return [
            user
            for user
            in self.users.values()
        ]

    def change_password(self, new_password: str, user_id: str) -> None:
        user = self.get_by_id(user_id)
        if user:
            user.password = new_password
            self.save(user)
    
    def delete(self, id: str) -> None:
        if id in self.users:
            del self.users[id]