# Created by jett at 9/27/17
Feature: Navigate Menus
  As an user with an account
  I want access to the pages of the app
  So that I can reach the app's functionality.

  Scenario: Reach the Login Page
    Given Application has been opened
    When I select "Login" menu item
    Then I see the "info" page
    And I wait "2" seconds

  Scenario: Reach the List Page
    Given Application has been opened
    When I select "List" menu item
    Then I see the "List" page
    And I wait "2" seconds

  Scenario: Reach the Map Page
    Given Application has been opened
     When I select "Map" menu item
     Then I see the "Map" page
      And I wait "2" seconds


