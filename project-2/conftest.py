import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox")

@pytest.fixture(scope="function")
def browserInstance (request):
    browser = request.config.getoption("--browser_name")

    if browser.lower() == "chrome":
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = (webdriver.Chrome
            (service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options))
    elif browser.lower() == "firefox":
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
    else:
        raise ValueError("Unsupported browser! Use 'chrome' or 'firefox'.")

    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only if the test failed
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browserInstance")
        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Error capturing screenshot: {e}")
