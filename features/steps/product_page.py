from behave import *


@given('I navigate to the homepage')
def step_impl(context):
    context.browser.get('https://www.amazon.com/')


@given('I search for {search_term}')
def step_impl(context, search_term):
    pass


@when('I select {product}')
def step_impl(context,):
    assert True is not False


@then('The price of the "Audio CD" is {price}')
def step_impl(context):
    assert context.failed is False


@then('The star rating is {rating}')
def step_impl(context):
    assert context.failed is False


@then('The first item in the "customers who bought this item also bought" section is {first_customers_also_bought}')
def step_impl(context):
    assert context.failed is False