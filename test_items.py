import pytest
import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


class TestProductPage:
    def test_add_to_basket_button(self, browser):
        browser.get(link)
        time.sleep(10)
        assert browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
