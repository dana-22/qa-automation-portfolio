from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()