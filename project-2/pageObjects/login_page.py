from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def open_modal(self):
        self.click((By.ID, "login2"))

    def login(self, username, password):
        self.type((By.ID, "loginusername"), username)
        self.type((By.ID, "loginpassword"), password)
        self.click((By.CSS_SELECTOR, "button[onclick='logIn()']"))

    def is_logged_in(self):
        return "Welcome" in self.get_text((By.ID, "nameofuser"))
