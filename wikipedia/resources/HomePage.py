from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
import time

class HomePage(PageObject):
    """Keywords for Wikipedia Home Page"""

    PAGE_TITLE = "Wikipedia"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "search_el": "id=searchInput",
    }


    def i_search_for_the_phrase(self, phrase):
        '''Searches for a phrase that does not match existing
           article titles'''
        self.se2lib.input_text(self.locator.search_el, phrase)
        self.se2lib.submit_form()
        time.sleep(5)
