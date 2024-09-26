import string

from selenium.webdriver.ie.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, base_url: string):
        self.driver = driver
        self.__base_url = base_url

    def get_base_url(self):
        return self.__base_url
