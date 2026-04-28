Feature: User Login
  As a user
  I want to log in to the application
  So that I can access my account

  Background:
    Given the login page is open

  Scenario: Successful login with valid credentials
    When I enter username "admin"
    And I enter password "admin123"
    And I click the login button
    Then I should see the dashboard

  Scenario: Failed login with invalid password
    When I enter username "admin"
    And I enter password "wrongpassword"
    And I click the login button
    Then I should see an error message

  Scenario: Login with empty username
    When I leave username empty
    And I enter password "admin123"
    And I click the login button
    Then I should see a validation error

  Scenario: Login with empty password
    When I enter username "admin"
    And I leave password empty
    And I click the login button
    Then I should see a validation error
