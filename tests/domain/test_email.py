import pytest
from src.users.domain.value_objects.email import Email


@pytest.mark.parametrize("email_str", ["example@gmail.com", "gus@gmail.com", "samujrs@gmail.com"])
def test_it_creates_email_correctly(email_str: str):
    email = Email(email_str)
    assert email.email == email_str


@pytest.mark.parametrize("email_str", ["", " ", "invalid-email", "example@.com", "@gmail.com", "example@com"])
def test_it_raises_when_email_is_invalid(email_str: str):
    assert Email.is_email_correct(email_str) is False