"""Pytest configuration."""
import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import SubRequest


def pytest_addoption(parser: Parser) -> None:
    """Add pytest options."""
    parser.addoption(
        '--full',
        action='store_true',
        default=False,
        help='run solution tests',
    )


@pytest.fixture
def full(request: SubRequest) -> bool:
    """Fixture for full option."""
    return bool(request.config.getoption('--full'))
