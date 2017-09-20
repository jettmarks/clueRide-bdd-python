# Created by jett at 9/17/17
Feature: Login via Form
  As an unauthenticated user with an existing account
  I want to supply my credentials
  So that I can start a session under my identity.

  Scenario: Valid Credentials are provided
    Given first access for a device
    When I open the application
    Then I see the "info" page
#     And I see a "Guest" badge
     And I see a "login" form

    When I enter my username and password
     And Click Login
#    Then I see a "Steward" badge
    Then I see a "logout" form

    When I revisit the application
    Then I see the "Map" page