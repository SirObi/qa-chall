from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
import time

class HomePage(PageObject):
    """Keywords for the Home page of Travelex"""

    PAGE_TITLE = "Currency Exchange | Buy Travel Money | Travelex"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "second_slide": "css=.slick-slider > ul > li:nth-child(2) > button",
        "third_slide": "css=.slick-slider > ul > li:nth-child(3) > button",
        "current_slide": "css=.slick-slide.slick-active > div > h4 > span > a"
    }

    def i_am_using_a_device_of_size(self, d_width, d_height):
        self.se2lib.set_window_size(d_width, d_height)

    def i_swipe_through_main_products_section(self):
        self.se2lib.click_element(self.locator.second_slide)
        self.se2lib.click_element(self.locator.third_slide)

    def i_see_the_appropriate_product(self):
        self.se2lib.element_text_should_be(self.locator.current_slide, "Buy foreign currency")
        time.sleep(5)
