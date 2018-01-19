from PageObjectLibrary import PageObject

class HomePage(PageObject):
    """Keywords for the Main Page for English wikipedia"""

    PAGE_TITLE = "Wikipedia, the free encyclopedia"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
    }
