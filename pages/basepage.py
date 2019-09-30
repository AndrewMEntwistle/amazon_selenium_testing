from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.browser = driver
        self.wait = WebDriverWait(driver=self.browser, timeout=10)
