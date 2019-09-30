from behave import *

from pages.homepage import Homepage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage


@given('I navigate to the homepage')
def step_impl(context):
    homepage = Homepage(context.browser)
    homepage.navigate_to()


@given('I search for {search_term}')
def step_impl(context, search_term):
    homepage = Homepage(context.browser)
    homepage.search(search_term)


@when('I select {product}')
def step_impl(context, product):
    search_results_page = SearchResultsPage(context.browser)
    search_results_page.select_product(product)


@then('The price of the "Audio CD" is {price}')
def step_impl(context, price):
    product_page = ProductPage(context.browser)
    product_page.assert_price_of_audio_cd(price)


@then('The star rating is {rating}')
def step_impl(context, rating):
    product_page = ProductPage(context.browser)
    product_page.assert_star_rating(rating)


@then(
    'The first item in the "customers who bought this item also bought" section is {first_item_customers_also_bought}')
def step_impl(context, first_item_customers_also_bought):
    product_page = ProductPage(context.browser)
    product_page.assert_first_item_customers_also_bought(first_item_customers_also_bought)
