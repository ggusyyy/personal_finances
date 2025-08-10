from dataclasses import dataclass
import re


@dataclass
class Email:
    email: str
    
    @staticmethod
    def is_email_correct(email: str) -> bool:
        __pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(__pattern, email) is not None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Email):
            return NotImplemented
        return self.email.lower() == other.email.lower()
    
    def __repr__(self) -> str:
        return self.email
    
    def __str__(self) -> str:
        return self.email