from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome("C:/Users/1083517/Downloads/chromedriver_win32 (1)/ChromeDriver.exe") #make an env variable for chromedriver
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)