from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, webdriver):
        self.browser = webdriver
        self.wait = WebDriverWait(driver=self.browser, timeout=10)
