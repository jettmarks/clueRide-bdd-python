# Created by jett at 2/20/18
Feature: Navigation from Rolling Page
  As a Game Player while Rolling
  I should be able to find the Location and Puzzle pages
  So I can easily play the game

  Scenario: Tapping Location brings up Location Page
    Given Registered Device
      And Application has been opened
      And I select "Play Game" menu item
     When I find the Test Marker
      And Click found Marker
     Then I see the "Location" page

  Scenario: Arrival should bring up Puzzle Page
    Given Registered Device
      And Application has been opened
      And I select "Play Game" menu item
     When Guide sends "Arrived" signal
     Then I see the "Puzzle" page
