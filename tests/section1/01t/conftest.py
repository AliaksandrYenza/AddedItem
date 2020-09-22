import time

from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: en-gb or ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options = Options()
        if language == 'ru':
            options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        elif language == 'en-gb':
            options.add_experimental_option('prefs', {'intl.accept_languages': 'en-gb'})
        else:
            raise pytest.UsageError("--language should be en-gb or ru")
        browser = webdriver.Chrome(options=options)


    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")

        fp = webdriver.FirefoxProfile()

        if language == 'ru':
            fp.set_preference("intl.accept_languages", 'ru')
        elif language == 'en-gb':
            fp.set_preference("intl.accept_languages", 'en-gb')
        else:
            raise pytest.UsageError("--language should be en-gb or ru")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")

    yield browser

    print("\nquit browser..")

    time.sleep(3)

    browser.quit()