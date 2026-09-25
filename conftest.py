import pytest
import json
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    """Initializes the browser session."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # Attach driver to calling test class context
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def data_load():
    """Loads external framework configuration data objects."""
    with open("config/test_data.json", "r") as file:
        return json.load(file)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hooks into test runtime failures to auto-capture execution snapshots."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "setup" in item.fixturenames:
            web_driver = item.funcargs['request'].cls.driver
            import os
            os.makedirs("reports/failures", exist_ok=True)
            web_driver.save_screenshot(f"reports/failures/{item.name}.png")
