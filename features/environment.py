import os
from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_browser_chrome(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    if os.environ.get('WEBDRIVER'):
        context.browser = webdriver.Chrome(os.environ.get('WEBDRIVER'), chrome_options=chrome_options)
    else:
        context.browser = webdriver.Chrome(chrome_options=chrome_options)
    context.browser.implicitly_wait(10)
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
