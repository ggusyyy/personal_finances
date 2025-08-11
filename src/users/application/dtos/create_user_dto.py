from dataclasses import dataclass


@dataclass
class CreateUserDTO:
    username: str
    email: str
    password: str