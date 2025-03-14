import requests
from behave import given, when, then
import json

# Step for setting the URL (this will store the URL in the context)
@given('the URL {url}')
def step_impl(context, url):
    context.url = url

# Step for sending a GET request
@when('I send a GET request')
def step_impl(context):
    context.response = requests.get(context.url)

# Step for checking if the status code is 200
@then('the status code should be 200')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"

# Step for matching the first item's id to be 1
@then('the response body should match the first item\'s id == 1')
def step_impl(context):
    response_json = context.response.json()
    assert response_json[0]['id'] == 1, f"Expected id 1 but got {response_json[0]['id']}"

# Step for matching the first item's title
@then('the response body should match the first item\'s title')
def step_impl(context):
    response_json = context.response.json()
    expected_title = 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
    assert response_json[0]['title'] == expected_title, f"Expected title to be '{expected_title}' but got '{response_json[0]['title']}'"
