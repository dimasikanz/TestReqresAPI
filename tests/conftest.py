import pytest

from lib.constants import CommonConstants
from lib.lib_api.api.apiclient import ApiClient


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


@pytest.fixture(scope="session")
def api_client(config):
    """
    Апи клиент описан здесь, т.к. он нужен и в api тестах, и в ui тестах
    """
    return ApiClient(base_url=config["url"])
