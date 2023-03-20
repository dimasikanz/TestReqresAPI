import pytest

from lib import constants
from api.apiclient import ApiClient
from lib.builder import Builder


def pytest_addoption(parser):
    """Парсер для чтения параметров из консоли"""
    parser.addoption("--url", default=constants.DEFAULT_URL)


@pytest.fixture(scope="session")
def config(request):
    """
    Вынос спарсенных из консоли параметров в словарь "config"
    """
    url = request.config.getoption("--url")

    return {
        "url": url
    }


@pytest.fixture(scope="session")
def api_client(config):
    return ApiClient(
        base_url=config["url"]
    )


@pytest.fixture(scope="session")
def builder():
    return Builder()