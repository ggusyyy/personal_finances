from users.application.dtos.create_user_dto import CreateUserDTO

from faker import Faker


class CreateUserDTOMother:

    faker = Faker()

    @classmethod
    def create(
        cls,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
    ) -> CreateUserDTO:
        username = username or cls.faker.user_name()
        email = email or cls.faker.email()
        password = password or cls.faker.password()

        return CreateUserDTO(username, email, password)
