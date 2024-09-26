from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class TwitchPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver, "https://www.twitch.tv")

    def get_mobile_url(self):
        return self.get_base_url().replace("www", "m")

    def get_popup_dismiss_btn(self):
        dismiss_btn_xpath = "//*[text()='Dismiss']/ancestor::button"
        return self.driver.find_element(By.XPATH, dismiss_btn_xpath)

    def get_search_icon(self):
        search_btn_xpath = "//button[@icon='NavSearch']|//a[@aria-label='Search']"
        return self.driver.find_element(By.XPATH, search_btn_xpath)


    def get_search_input(self):
        wait = WebDriverWait(self.driver, 3)
        search_input_xpath = "//input[@type='search']"
        return wait.until(EC.element_to_be_clickable((By.XPATH, search_input_xpath)))


    def get_streamers_thumbnails(self):
        streamers_thumbnails = """
                                //a[contains(@class,'tw-link') and \n
                                not(contains(@href,'search?')) and \n
                                not(contains(@href,'/category'))]
                                """
        wait = WebDriverWait(self.driver, 3)
        return wait.until(EC.visibility_of_all_elements_located((By.XPATH, streamers_thumbnails)))


    def get_videoplayer_elements(self):
        video_player_elements_xpath = "//div[contains(@class,'video-player')]"
        wait = WebDriverWait(self.driver, 3)
        return wait.until(EC.visibility_of_all_elements_located((By.XPATH, video_player_elements_xpath)))

    def dismiss_popup(self):
        self.get_popup_dismiss_btn().click()
        sleep(2)


    def search(self, search_term):
        self.get_search_icon().click()
        search_input = self.get_search_input()
        search_input.click()
        search_input.clear()
        search_input.send_keys(search_term, Keys.ENTER)
