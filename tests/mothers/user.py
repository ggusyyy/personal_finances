from faker import Faker

from datetime import datetime
from users.domain.user import User
from users.domain.value_objects.email import Email


class UserMother:

    faker = Faker()

    @classmethod
    def create(
        cls,
        id: str | None = None,
        username: str | None = None,
        email: str | None = None,
        password: str | None = None,
        created_at: datetime | None = None
    ) -> User:
        id = id or cls.faker.uuid4()
        username = username or cls.faker.user_name()
        email = email or cls.faker.email()
        password = password or cls.faker.password()
        created_at = created_at or cls.faker.date_time()

        return User(id, username, Email(email), password, created_at)
