import logging
import os
import string
from pathlib import Path

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

import main

LOGGER = logging.getLogger(__name__)

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
    LOGGER.info("Webdriver started.")
    yield driver
    take_screenshot(driver, request.node.name, "png")
    driver.close()
    driver.quit()
    LOGGER.info("Webdriver terminated.")


def prepare_browser_options(conf):
    options = None
    if conf['browser'] == 'chrome':
        options = webdriver.ChromeOptions()
        if conf['mobile_emulation']['enabled'] is True:
            mobile_emulation = {
                "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
            }
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            LOGGER.info("Mobile emulation enabled.")

    return options


def assert_chrome_browser(browser_name: string):
    assert browser_name.upper() == 'CHROME',  "Only Chrome browser is available"


def take_screenshot(driver: WebDriver, screenshot_name: string, format: string):
    screenshots_path = f"{os.path.dirname(main.__file__)}/screenshots/"
    Path(screenshots_path).mkdir(parents=True, exist_ok=True)
    screenshots_path = Path(f"{screenshots_path}{screenshot_name}.{format.lower()}")
    LOGGER.info(f"Saving screenshot in {screenshots_path}")
    driver.get_screenshot_as_file(f"{screenshots_path}")


def test_hello_world(driver):
    driver.get("https://google.com")

