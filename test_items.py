from selenium.webdriver.common.by import By
import time
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_should_be_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(5)
    button_add_to_cart = browser.find_element(By.XPATH, '//form[@id = "add_to_basket_form"]//button')
    assert button_add_to_cart.is_enabled() , 'The button is not available!'

# commit 7 december

