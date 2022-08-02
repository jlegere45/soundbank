import pytest
from src.database import users

def test_insert_user(username1, email1):
    result = users.insert_user(username1, email1, "password")
    assert result[0] > 1
    assert result[1] == username1
    assert result[2] == email1

def test_get_user(username2, email2, test_user):
    result = users.get_user(id=test_user)
    assert result[0] == test_user
    assert result[1] == username2
    assert result[2] == email2
    result = users.get_user(username=username2)
    assert result[0] == test_user
    assert result[1] == username2
    assert result[2] == email2
    result = users.get_user(email=email2)
    assert result[0] == test_user
    assert result[1] == username2
    assert result[2] == email2

def test_delete_user(username1, email1):
    users.delete_user(username=username1, email=email1)