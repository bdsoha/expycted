import pytest
from helpers.utils import CONTEXT


@pytest.fixture(scope="session")
def context():
    return CONTEXT
