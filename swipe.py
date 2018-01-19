from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DEVICE_SIZE = (550, 550)
browser = webdriver.Chrome()

def swipe(locator, direction):
    '''Implements swipe-like sequence of actions on a WebElement
       Accepts css selector and direction ('left' or 'right')'''
    actions = webdriver.common.action_chains.ActionChains(browser)
    element = browser.find_element_by_css_selector(locator)
    el_width = element.size['width']

    if direction == 'right':
        offset_x = el_width/2
    elif direction == 'left':
        offset_x = el_width/-2

    actions.move_to_element(element)
    actions.click_and_hold(element)
    actions.move_by_offset(offset_x, 0)
    actions.release()
    actions.perform()

browser.get('https://www.travelex.co.uk/')
browser.set_window_size(DEVICE_SIZE[0], DEVICE_SIZE[1])

n_swipes = 2
for i in range(n_swipes):
    swipe('.slick-slider', 'left')
assert browser.find_element_by_css_selector('.slick-slider .slick-slide[index="%s"]' % str(n_swipes + 1))
browser.quit()
