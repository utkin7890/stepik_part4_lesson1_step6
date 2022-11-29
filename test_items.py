import pytest
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.XPATH, "//button[@value = 'Добавить в корзину']")
    time.sleep(5)