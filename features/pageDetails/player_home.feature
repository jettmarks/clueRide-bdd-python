# Created by jett at 1/28/18
Feature: Player Home Page
  As a Game Player
  My Home page should orient me
  So I know at a glance what the upcoming Outing is about

  Scenario: Complete list of Info available on Home Page
    Given Registered Device
      And Application has been opened
     When I select "Home" menu item
      And I wait "1" seconds
     Then I see the "Home" page
      And I see a "Outing" section heading
      And I see a link to "Five Free Things"
      And I see a "Registered As" section heading
      And I see a "Badges" section heading
      And I see the "Begin Game" button


