import logging
from time import sleep

import pytest

from pages.twitch_page import TwitchPage
from utils.driver import driver, config

LOGGER = logging.getLogger(__name__)
SEARCH_TERM = "StarCraft II"

def test_mobile_search(driver):
    skip_non_mobile_test(driver)

    twitch_page = TwitchPage(driver)

    LOGGER.info(f"Visiting {twitch_page.get_mobile_url()}.")
    driver.get(twitch_page.get_mobile_url())

    LOGGER.info(f"Searching for {SEARCH_TERM}")
    twitch_page.search(SEARCH_TERM)
    assert twitch_page.get_search_input().get_attribute('value') == SEARCH_TERM, \
        f"Search input did not retain the searched term {SEARCH_TERM}"

    LOGGER.info(f"Scrolling down twice.")
    for n in range(2):
        driver.execute_script("window.scrollBy(0, 100)")

    LOGGER.info("Attempting to click a streamer from the search results.")
    streamer_index       = 0
    streamers_thumbnails = twitch_page.get_streamers_thumbnails()
    stream_url           = streamers_thumbnails[streamer_index].get_attribute('href')
    streamers_thumbnails[streamer_index].click()
    sleep(5)

    assert driver.current_url.__contains__(stream_url) , f"""
            Clicking on the search result {streamer_index} did not redirect to the expected URL.\n
            Expected [{stream_url}]\n
            Found [{driver.current_url}]
        """
    assert len(twitch_page.get_videoplayer_elements()) > 0 , "No video player elements present."
    LOGGER.info(f"Successfully redirected to stream page.")

    try:
        twitch_page.dismiss_popup()
        LOGGER.info("Popup dismissed.")
    except Exception:
        LOGGER.info("No popup dismiss button shown.")


def skip_non_mobile_test(driver):
    if(config()['mobile_emulation']['enabled']) is False:
        pytest.skip("This test is meant for mobile view only.")
