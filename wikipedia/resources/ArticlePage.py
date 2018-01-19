from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

class ArticlePage(PageObject):
    """Keywords for an article page on wikipedia"""

    PAGE_TITLE = "Rabbit Bandini Productions - Wikipedia"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
        "article_title": "id=firstHeading",
        "table_contents": "id=toc",
    }

    def i_see_a_title(self):
        self.se2lib.page_should_contain_element(self.locator.article_title)

    def i_see_a_table_of_contents(self):
        self.se2lib.page_should_contain_element(self.locator.table_contents)
