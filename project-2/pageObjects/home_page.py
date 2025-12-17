from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def add_product(self, name):
        self.driver.get("https://www.demoblaze.com/")
        self.click((By.LINK_TEXT, name))
        self.click((By.LINK_TEXT, "Add to cart"))
        self.accept_alert()

    def go_to_cart(self):
        self.click((By.ID, "cartur"))