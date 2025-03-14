Feature: API Testing for POST and GET

  Scenario: Test the Login API
    Given the URL https://jsonplaceholder.typicode.com/posts
    When I send a GET request
    Then the status code should be 200
    And the response body should match the first item's id == 1
    And the response body should match the first item's title
