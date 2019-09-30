from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .basepage import BasePage
from .product_page import ProductPage


class SearchResultsPage(BasePage):

    def __init__(self, webdriver):
        super(SearchResultsPage, self).__init__(webdriver)

    def wait_until_page_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='s-result-list s-search-results sg-row']")))

    def select_product(self, product):
        product_page = ProductPage(self.browser)
        self.browser.find_element_by_xpath(f"//span[contains(text(), '{product}')]").click()
        product_page.wait_until_page_loaded()
