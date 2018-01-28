from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

class ResultsPage(PageObject):
    """Keywords for Wikipedia Results Page"""

    PAGE_TITLE = "Search results - Wikipedia"
    PAGE_URL = ""

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "results_list": "css=.mw-search-results",
        "suggestion_el": "css=.searchdidyoumean > a",
        "search_suggestion": "css=.searchdidyoumean > a",
        "search_results": "css=.mw-search-results .mw-search-result-heading > a"
    }

    def i_see_a_list_of_results(self):
        self.se2lib.page_should_contain_element(self.locator.results_list)

    def i_see_a_search_suggestion(self):
        self.se2lib.page_should_contain_element(self.locator.search_suggestion)

    def i_click_on_the_search_suggestion(self):
        self.se2lib.click_element(self.locator.search_suggestion)

    def the_number_of_results_is(self, number):
        self.se2lib.page_should_contain_element(self.locator.search_results, limit=number)

    def i_click_on_the_first_result(self):
        self.se2lib.click_element(self.locator.search_results)
