from hamcrest import assert_that, equal_to
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers.selector_helper import SelectorHelper

from .basepage import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
        self.first_carousel_item = "li[class='a-carousel-card'][aria-posinset='1']"

    def wait_until_page_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class='a-size-large a-spacing-micro']")))

    def assert_price_of_audio_cd(self, price):
        audio_cd_box_child = self.browser.find_element_by_xpath(
            "//a[@class='a-button-text']/span[contains(text(), 'Audio CD')]")
        audio_cd_box = SelectorHelper.get_parent_of_element(audio_cd_box_child)
        audio_cd_box_price = audio_cd_box.find_element_by_xpath(".//span[@class='a-size-base a-color-secondary']").text
        assert_that(audio_cd_box_price, equal_to(price))

    def assert_star_rating(self, expected_rating):
        rating_text = self.browser.find_element_by_css_selector('#acrPopover').get_attribute('title')
        found_rating = rating_text[0:3]
        assert_that(found_rating, equal_to(expected_rating))

    def assert_first_item_in_customers_also_bought(self, first_item_customers_also_bought):
        actions = ActionChains(self.browser)
        first_carousel_item = self.browser.find_element_by_css_selector(self.first_carousel_item)
        actions.move_to_element(first_carousel_item).perform()
        loaded_first_carousel_item = self.browser.find_element_by_css_selector(self.first_carousel_item)
        first_item_text = loaded_first_carousel_item.find_element_by_xpath("./a/span").text
        assert_that(first_item_text, equal_to(first_item_customers_also_bought))
