# Created by jett at 10/3/17
Feature: Single point-of-entry for Location Type
  User Story CA-312:
  As an App Maintainer,
  I want to add a location in a single place,
  So all of the application has it available with the data it needs.

  Scenario: REST API retrieves List of Location Types
    When I request Location Types
    Then I can list out Location Types

  Scenario: Edit pull-down shows complete list of Location Types
    Given the "Map" page has been opened
     When I request Location Types
      And I list all items in the select field labeled "Type"
     Then the two lists match

  Scenario: Icons are shown on Markers
    Given the "Map" page has been opened
     When I find the Test Marker
      And I read the Location Type
     Then I see an icon matching the Location Type

  Scenario Outline: Each <Location Type> has appropriate <Icon>
    Given the "Map" page has been opened
     When I set the Test Marker's "Type" to "<Name>"
     Then I find the Test Marker
      And I read the "<Location Type>"
      And I see the "<Icon>" matches
    Examples:
      | Name       | Location Type | Icon    |
      | Picnic     | PICNIC        | basket  |
      | Bike Share | BIKE_SHARE    | bicycle |

