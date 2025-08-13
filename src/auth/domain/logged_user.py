from dataclasses import dataclass


@dataclass
class LoggedUser:
    id: str
    username: str