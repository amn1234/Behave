Feature: API testing

  Scenario: Test GET request
    Given I make a GET request to "https://jsonplaceholder.typicode.com/posts"
    Then the response status code should be 200
    And the response body should contain "userId"
