# Created by jett at 1/1/18
Feature: Register an un-registered App
  As a new Member who has just installed the App
  I am prompted to register the App
  So I can use the App and provide my email address for badge issuance.

  Scenario: Unregistered App presents Registration Page
    Given Application has been opened
     When I wait for page with "welcome" ID
      And I wait "1" seconds
     Then I see the "Registration" page

  Scenario: Verify options on Registration Page
    Given Application has been opened
     When I wait for page with "welcome" ID
     Then I see the "Register via Email" button
      And I see the "Register via Google or Facebook" button

  Scenario: Register the App presents Confirm Email Page
    Given Application has been opened
     When I wait for page with "welcome" ID
      And I wait "1" seconds
      And I click the "BDD Mock Register" link
      And I wait for page with "confirm" ID
      And I wait "1" seconds
     Then I see the "Confirm Email" page

  Scenario: Verify options on Confirm Email Page
    Given Application has been opened
      And Application is unregistered -- and refreshed
      And I wait "1" seconds
     When I click the "BDD Mock Register" link
      And I wait for page with "confirm" ID
      And I wait "1" seconds
     Then I see the "Confirm Email" page
      And I see the "Use this Email" button
      And I see the "Choose different Email" button

  Scenario: Register and Confirm leads to Home page
    Given Application has been opened
      And Application is unregistered -- and refreshed
      And I wait "1" seconds
     When I click the "BDD Mock Register" link
      And I wait for page with "confirm" ID
      And I wait "1" seconds
      And I click the "Use this Email" button
      And I wait "1" seconds
     Then I see the "Home" page

  Scenario: Register and Choose different Email
    Given Application has been opened
      And Application is unregistered -- and refreshed
      And I wait "1" seconds
     When I click the "BDD Mock Register" link
      And I wait for page with "confirm" ID
      And I wait "1" seconds
      And I click the "Choose Different Email" button
      And I wait "1" seconds
     Then I see the "Registration" page
