# Created by jett at 12/24/17
Feature: View Register Device Email Links
  As a user receiving an initial invite email
  I want to view the steps to register my device
  So I know what needs to be done.

  Scenario: Invite Email has Register Device links
    Given Email with name "New Player Invite" has been received
     When I open the link for "How to Register your Device"
     Then I see the "How to Register your Device – Clue Ride" page
    # NOTE: There is an m-dash in the title: ' – '




