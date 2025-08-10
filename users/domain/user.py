from dataclasses import dataclass
from datetime import datetime

from users.domain.value_objects.email import Email

@dataclass
class User:
    id: str
    username: str
    email: Email
    password: str
    created_at: datetime