from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.XPATH, "//form[@id = 'add_to_basket_form']//button")
    time.sleep(5)