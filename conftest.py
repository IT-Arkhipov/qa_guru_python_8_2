import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_init():
    browser.config.window_width=1920
    browser.config.window_height=1080
    # or browser.config.driver.maximize_window()

    yield

    browser.quit()
