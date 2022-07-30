import pytest
from src.database import users


@pytest.fixture
def username1():
    return "Bob Johnson"

@pytest.fixture
def email1():
    return "BobJ@gmail.com"

@pytest.fixture
def username2():
    return "John Johnson"

@pytest.fixture
def email2():
    return "JohnJ@gmail.com"

@pytest.fixture
def test_user(username2, email2):
    result = users.insert_user(username2, email2)
    yield result[0]
    users.delete_user(id=result[0])

    