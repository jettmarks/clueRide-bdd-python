# Created by jett at 12/25/17
Feature: View Install App Email Links
  As a user receiving an initial invite email
  I want to view the steps to install the mobile app on my device
  So I can play the game.

  Scenario: Invite Email has Install App Links
    Given Email with name "New Player Invite" has been received
    When I open the link for "Installation Instructions"
    Then I see the "How to Install Clue Ride – Clue Ride" page
    # NOTE: There is an m-dash in the title: ' – '
