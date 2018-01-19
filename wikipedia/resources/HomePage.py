from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

class HomePage(PageObject):
    """Keywords for Wikipedia Home Page"""

    PAGE_TITLE = "Wikipedia"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "search_el": "id=searchInput",
        "wikipedia_logo": "css=.mw-wiki-logo",
        "language_link": 'css=#p-lang a[lang="%s"]',

    }

    def i_search_for_the_phrase(self, phrase):
        '''Searches for a phrase that does not match existing
           article titles'''
        self.se2lib.input_text(self.locator.search_el, phrase)
        self.se2lib.submit_form()

    def i_go_to_main_page(self):
        self.se2lib.click_element(self.locator.wikipedia_logo)

    def i_change_the_language_to(self, language):
        self.se2lib.click_element(self.locator.language_link % language)
