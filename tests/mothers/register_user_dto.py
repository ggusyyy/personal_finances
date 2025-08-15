
from faker import Faker

from src.auth.application.dtos.register_user_dto import RegisterUserDTO


class RegisterUserDTOMother:

    faker = Faker()

    @classmethod
    def create(
        cls,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
    ) -> RegisterUserDTO:
        username = username or cls.faker.user_name()
        email = email or cls.faker.email()
        password = password or cls.faker.password()

        return RegisterUserDTO(username, email, password)
