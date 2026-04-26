import pytest
from faker import Faker
faker = Faker()

@pytest.fixture()
def user():

    username = faker.user_name()
    return username


