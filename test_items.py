import pytest
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(50)