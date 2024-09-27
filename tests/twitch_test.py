import logging
from time import sleep

import pytest

from pages.twitch_page import TwitchPage
from utils.driver import driver, config

LOGGER       = logging.getLogger(__name__)
SEARCH_TERM  = "StarCraft II"
MAX_ATTEMPTS = 3

def test_mobile_search(driver):
    skip_non_mobile_test(driver)
    perform_streamer_search(TwitchPage(driver))


def perform_streamer_search(page: TwitchPage, attempts=0):
    eval_attempts(attempts)
    try:
        LOGGER.info(f"Visiting {page.get_mobile_url()}.")
        page.driver.get(page.get_mobile_url())

        LOGGER.info(f"Searching for {SEARCH_TERM}")
        page.search(SEARCH_TERM)
        assert page.get_search_input().get_attribute('value') == SEARCH_TERM, \
            f"Search input did not retain the searched term {SEARCH_TERM}"

        LOGGER.info(f"Scrolling down twice.")
        for n in range(2):
            page.driver.execute_script("window.scrollBy(0, 100)")

        LOGGER.info("Attempting to click a streamer from the search results.")
        result_index = 0
        thumbnails   = page.get_streamers_thumbnails()
        stream_url   = thumbnails[result_index].get_attribute('href')
        thumbnails[result_index].click()
        sleep(5)

        assert page.driver.current_url.__contains__(stream_url), f"""
                    Clicking on the search result {result_index} did not redirect to the expected URL.\n
                    Expected [{stream_url}]\n
                    Found [{page.driver.current_url}]
                """

        assert len(page.get_videoplayer_elements()) > 0, "No video player elements present."
        LOGGER.info(f"Successfully redirected to stream page.")

        dismiss_popup(page)

    except:
        attempts = attempts + 1
        LOGGER.info(f"Failed to search. Retrying [{attempts}/{MAX_ATTEMPTS}]")
        perform_streamer_search(page, attempts)


def skip_non_mobile_test(driver):
    if(config()['mobile_emulation']['enabled']) is False:
        pytest.skip("This test is meant for mobile view only.")


def eval_attempts(attempts):
    if attempts == MAX_ATTEMPTS:
        raise Exception(f"Unable to search for streamer. Max attempts reached {attempts}")

def dismiss_popup(page:TwitchPage):
    try:
        page.dismiss_popup()
        LOGGER.info("Popup dismissed.")
    except:
        LOGGER.info("No popup dismiss button shown.")
