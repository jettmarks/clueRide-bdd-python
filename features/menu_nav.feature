# Created by jett at 1/27/18
Feature: Navigate the Menu
  As a Game Player
  I want to have access to the various pages
  So I can find my way around the application

  Scenario: From Menu, reach the Home Page
    Given Registered Device
      And Application has been opened
     When I select "Home" menu item
     Then I see the "Home" page

  Scenario: From Menu, reach the Team Page
    Given Registered Device
      And Application has been opened
     When I select "Team" menu item
     Then I see the "Team" page

  Scenario: From Menu, reach the Outing Page
    Given Registered Device
      And Application has been opened
     When I select "Outing" menu item
     Then I see the "Outing" page

  Scenario: From Menu, reach the Badges Page
    Given Registered Device
      And Application has been opened
     When I select "Badges" menu item
     Then I see the "Badges" page
