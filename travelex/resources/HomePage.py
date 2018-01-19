from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn

class HomePage(PageObject):
    """Keywords for the Home page of Travelex"""

    PAGE_TITLE = "Currency Exchange | Buy Travel Money | Travelex"
    PAGE_URL = "/"

    # these are accessible via dot notaton with self.locator
    # (eg: self.locator.username, etc)
    _locators = {
    }
