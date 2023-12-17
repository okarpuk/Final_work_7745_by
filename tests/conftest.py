import pytest

@pytest.fixture()
def set_up():
    print("\n***** TEST STARTED *****")
    yield
    print("\n***** TEST FINISHED *****")