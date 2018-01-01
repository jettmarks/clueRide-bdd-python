# Created by jett at 9/19/17
Feature: Edit Location
  As an authenticated user with Steward badge
  I want to make changes to a Location
  So that I can raise the location's readiness level.

  Scenario: Brand New Location needing all values
    Given the "Map" page has been opened
     When I find the Test Marker
      And Click found Marker
     Then I see the "Editing:" page

  Scenario: Change Location Type
    Given the "Map" page has been opened
     When I find the Test Marker
      And Click found Marker
     Then I see the "Editing:" page

     When I see the "select" class labeled "Type"
      And I enter "Picnic" into the "select" field labeled "Type"
      And I Click the alert's "OK" button
     Then I see the "Editing:" page
      And I see the text "Picnic" in the "select" field labeled "Type"
     Then I Click the edit form's "Save" button

     When I refresh the map page
      And I find the Test Marker
      And Click found Marker
     Then I see the "Editing:" page
      And I see the "select" class labeled "Type"
      And I see the text "Picnic" in the "select" field labeled "Type"

  Scenario: Change Selected Image
    Given the "Map" page has been opened
     When I find the Test Marker
      And Click found Marker
     Then I see the "Editing:" page

    When I see the "img" field labeled "Featured Image"
     And I Click the image edit's "New Image" button
    Then I see the "Image:" page

  Scenario: Add Lock
    Given the "Map" page has been opened
     When I find the Test Marker
      And Click found Marker
     Then I see the "Editing:" page

     When I select the "Locks" tab
      And I Click the edit form's "New Lock" button

