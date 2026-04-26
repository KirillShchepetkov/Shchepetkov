import pytest

class TestExample:

    @pytest.mark.regression
    def test_example(self, user):
        print(user)

