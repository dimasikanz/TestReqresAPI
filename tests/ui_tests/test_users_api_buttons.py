import time
import pytest

@pytest.mark.ui
class TestUsersApiButtons:
    def test_go_to_the_page(self, main_page):
        time.sleep(5)