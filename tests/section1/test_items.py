import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAddTest():

    @pytest.mark.parametrize('link', "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    def test_b(self, browser, link):
        browser.get(link)
        #browser.implicitly_wait(10)


"""        bnt = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket'))
        )
        bnt.click()

        restxt = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket'))
        ).text

        original_total = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='basket-mini pull-right hidden-xs']/text()[2]"))
        ).text
        expected_res = original_total + 19.99

        assert restxt, expected_res"""
