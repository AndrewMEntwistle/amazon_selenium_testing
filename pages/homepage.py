from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from .basepage import BasePage
from .search_results_page import SearchResultsPage


class Homepage(BasePage):

    def __init__(self, driver):
        super(Homepage, self).__init__(driver)
        self.search_bar = '#twotabsearchtextbox'

    def navigate_to(self):
        self.browser.get('https://www.amazon.com/')
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search_bar)))

    def search(self, search_term):
        search_results_page = SearchResultsPage(self.browser)
        search_bar = self.browser.find_element_by_css_selector(self.search_bar)
        search_bar.send_keys(search_term, Keys.RETURN)
        search_results_page.wait_until_page_loaded()
