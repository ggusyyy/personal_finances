from dataclasses import dataclass


@dataclass
class RegisterUserDTO:
    username: str
    email: str
    password: str