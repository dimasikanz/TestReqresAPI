import pytest
from lib.constants import CommonConstants

def pytest_addoption(parser):
    """Парсер для чтения параметров из консоли"""
    parser.addoption("--url", default=CommonConstants.DEFAULT_URL)


@pytest.fixture(scope="session")
def config(request):
    """
    Вынос спарсенных из консоли параметров в словарь "config"
    """
    url = request.config.getoption("--url")

    return {"url": url}
