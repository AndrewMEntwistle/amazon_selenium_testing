from behave import fixture, use_fixture
from selenium import webdriver
import os


@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome(os.environ.get('WEBDRIVER'))
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)