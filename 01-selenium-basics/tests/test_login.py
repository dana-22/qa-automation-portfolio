import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()
def test_login_valid(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.XPATH, "//button[@id='submit']").click()

    assert "Logged In Successfully" in driver.page_source
    assert driver.current_url.endswith("logged-in-successfully/")

def test_username_invalid(driver):
    driver.refresh()
    driver.find_element(By.ID, "username").send_keys("incorrectUser")
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Password123")
    driver.find_element(By.CSS_SELECTOR, "button#submit").click()

    error = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error

def test_password_invalid(driver):
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("student")
    driver.find_element(By.NAME, "password").send_keys("incorrectPassword")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    error = driver.find_element(By.ID, "error").text
    assert "Your password is invalid!" in error
