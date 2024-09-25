import string
from pathlib import Path

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def config():
    path = Path(__file__).parent / "../conf/config.yaml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()

@pytest.fixture
def driver(request):
    conf = config()
    assert_chrome_browser(conf['browser'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=prepare_browser_options(conf))
    driver.implicitly_wait(10)
    yield driver
    # TODO: Screenshot
    driver.close()
    driver.quit()

def prepare_browser_options(conf):
    options = None

    if conf['browser'] == 'chrome':
        options = webdriver.ChromeOptions()

    return options


def assert_chrome_browser(browser_name: string):
    assert browser_name.upper() == 'CHROME',  "Only Chrome browser is available"
