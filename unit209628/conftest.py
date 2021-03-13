import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):

    # options to use drivers that are not specified in Windows PATH
    chrome_path = r"C:\Users\bazyakina\Desktop\Temp\pythonStepik\curs2\89.0.4389.23\chromedriver.exe"
    f_driver_path = r"C:\Users\bazyakina\Desktop\Temp\pythonStepik\curs2\geckodriver-v0.29.0-win64\geckodriver.exe"
    binary = FirefoxBinary(r'C:\Users\bazyakina\AppData\Local\Mozilla Firefox\firefox.exe')

    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        if os.path.exists(chrome_path):
            browser = webdriver.Chrome(executable_path=chrome_path, options=options)
        else:
            browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        if os.path.exists(f_driver_path):
            browser = webdriver.Firefox(executable_path=f_driver_path, firefox_binary=binary, firefox_profile=fp)
        else:
            browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()