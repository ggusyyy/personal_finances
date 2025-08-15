from dataclasses import dataclass


@dataclass
class LoginDTO:
    email: str
    password: str