Feature: Login
  Scenario: Successful login
    Given the user is on the Sauce Demo login page
    When the user logs in with valid credentials
    Then the user should be redirected to the inventory page
    Then click on logout button