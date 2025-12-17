import json
import pytest
from pageObjects.login_page import LoginPage
from pageObjects.home_page import HomePage
from pageObjects.cart_page import CartPage

with open("data/logins.json", "r", encoding="utf-8") as f:
    logins = json.load(f)

test_cases = []
for user in logins["valid"]:
    test_cases.append((user["username"], user["password"], True))
for user in logins["invalid"]:
    test_cases.append((user["username"], user["password"], False))

@pytest.mark.parametrize("username, password, expected_success", test_cases)
def test_demoblaze_e2e_with_json_logins(browserInstance, username, password, expected_success):
    driver = browserInstance

    login = LoginPage(driver)
    home = HomePage(driver)
    cart = CartPage(driver)

    login.open_modal()
    login.login(username, password)

    if not expected_success:

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert "Wrong password" in alert_text or "User does not exist" in alert_text
        except:
            pass
        print(f"Invalid login with {username} passed as expected")
        return


    assert login.is_logged_in()

    products = ["Samsung galaxy s6", "Nokia lumia 1520", "Sony vaio i5"]
    for product in products:
        home.add_product(product)

    home.go_to_cart()
    cart.delete_second_item()
    cart.place_order()

    print(f"Full E2E flow with user {username} PASSED!")