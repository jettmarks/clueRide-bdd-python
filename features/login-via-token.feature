# Created by jett at 9/17/17
Feature: Login via Token
  As a user holding a device that has logged in before
  I want to automatically open a session
  So I can avoid having to re-enter my credentials.

  Background: Auth Token for Steward role is within the browser's storage
    Given Application has been opened
      And Valid Token has been set
      And Valid Token has been checked

  Scenario: Valid Auth Token
    When I open the application
#    When I revisit the application
     And Valid Token has been checked
    Then I see the "ClueRide Location Editor" page

    When I wait for Map to load
    Then I see the "Map" page

    When I select "Info" menu item
    Then I see the "info" page
     And I see a "Steward" badge
