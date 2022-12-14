from __future__ import annotations

import pytest

from helpers.utils import Context


@pytest.fixture(scope="session")
def context():
    return Context()
