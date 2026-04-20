import pytest
from collections import namedtuple
from faker import Faker
faker = Faker()

@pytest.fixture
def user():

    login = faker.user_name()
    password = faker.password()
    User = namedtuple("_", ["login", "password"])
    return User(login, password)