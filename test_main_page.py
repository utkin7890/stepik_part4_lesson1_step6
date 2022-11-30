from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
import time



def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    page.is_element_present()
    time.sleep(3)





