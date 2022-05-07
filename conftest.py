import pytest
from selenium import webdriver
from pytest_html_reporter import attach


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\fccdp\\PycharmProjects\\seleniumTest\\drivers\\geckodriver.exe')
    driver.set_page_load_timeout(15)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True) #screenshot failures
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver_fixture = item.funcargs["driver"]
        attach(data=driver_fixture.get_screenshot_as_png())