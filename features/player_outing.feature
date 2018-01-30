# Created by jett at 1/29/18
Feature: Player Outing Page
  As a Game Player
  My Outing page should provide me with Outing details
  So I know where to be when the game starts

  Scenario: Complete list of Info available on Outing Page
    Given Registered Device
      And Application has been opened
     When I select "Outing" menu item
      And I wait "1" seconds
     Then I see the "Outing" page
      And I see a "Outing" section heading
      And I see a "Team" section heading
      And I see a "Meeting Location" section heading
      And I see the "Begin Game" button
