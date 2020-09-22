import time

import pytest
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test01t():


    #@pytest.mark.parametrize('link', "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    def test_click_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)


        btn_add = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket'))
        )
        btn_add.click()

        actual_res = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info'))
        )

        assert actual_res, True
