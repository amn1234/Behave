import requests
from behave import given, when, then
import json

# Store the response globally
response = None

@given('I make a GET request to "{url}"')
def step_impl_get_request(context, url):
    global response
    response = requests.get(url)

@then('the response status code should be {status_code:d}')
def step_impl_check_status_code(context, status_code):
    assert response.status_code == status_code, f"Expected {status_code}, but got {response.status_code}"

@then('the response body should contain "{key}"')
def step_impl_check_response_body(context, key):
    body = response.json()
    assert key in json.dumps(body), f"Expected key '{key}' in response, but it was not found"
