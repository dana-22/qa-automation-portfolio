from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def delete_second_item(self):

        second_item = self.driver.find_element(By.XPATH, "//tbody[@id='tbodyid']/tr[2]")
        delete_button = second_item.find_element(By.XPATH, ".//a[text()='Delete']")
        delete_button.click()
        WebDriverWait(self.driver, 10).until(  EC.staleness_of(second_item))
    def place_order(self):
        self.click((By.XPATH, "//button[text()='Place Order']"))
        self.type((By.ID, "name"), "João Silva")
        self.type((By.ID, "country"), "Portugal")
        self.type((By.ID, "city"), "Lisboa")
        self.type((By.ID, "card"), "4111111111111111")
        self.type((By.ID, "month"), "12")
        self.type((By.ID, "year"), "2028")
        self.click((By.XPATH, "//button[text()='Purchase']"))
        self.click((By.XPATH, "//button[text()='OK']"))