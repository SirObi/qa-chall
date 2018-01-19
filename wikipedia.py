from selenium import webdriver

browser = webdriver.Chrome()

def user_searches_for_articles_related_to_phrase():
    '''Searches for a phrase that does not match existing
       article titles'''
    browser.get('http://www.wikipedia.org')
    assert browser.title == 'Wikipedia'
    search_el = browser.find_element_by_id('searchInput')
    search_el.clear()
    search_el.send_keys('furry rabbits')
    search_el.submit()
    results_list = browser.find_element_by_css_selector('.mw-search-results')
    assert results_list
    suggestion_el = browser.find_element_by_css_selector('.searchdidyoumean > a')
    assert suggestion_el

def user_follows_search_suggestion():
    '''Tests whether search suggestion directs to new results list'''
    suggestion_el = browser.find_element_by_css_selector('.searchdidyoumean > a')
    suggestion_el.click()
    results = browser.find_elements_by_css_selector('.mw-search-results .mw-search-result-heading > a')
    assert len(results) == 20
    assert not suggestion_el

def user_opens_article_from_results_list():
    '''Opens article from results list and checks basic article structure'''
    results = browser.find_elements_by_css_selector('.mw-search-results .mw-search-result-heading > a')
    results[0].click()
    art_title = browser.find_element_by_id('firstHeading')
    assert art_title
    t_contents = browser.find_element_by_id('toc')
    assert t_contents

def user_changes_language(language):
    '''Tests subdomain change after selecting language'''
    main_page_logo = browser.find_element_by_css_selector('.mw-wiki-logo')
    main_page_logo.click()
    language_link = browser.find_element_by_css_selector('#p-lang a[lang="%s"]' % language)
    language_link.click()
    assert 'de.wikipedia.org' in browser.current_url


user_searches_for_articles_related_to_phrase()
user_follows_search_suggestion()
user_opens_article_from_results_list()
user_changes_language('de')

browser.quit()
