# Created by jett at 11/4/17
Feature: #Enter feature name here
  # Enter feature description here
  As a user with ability to add images
  I want to add images to a location

  Scenario: Ask to capture images using Camera
    # Enter steps here
    Given the "Map" page has been opened
     When I find the Test Marker
      And Click found Marker
     Then I see the "Editing:" page

    When I see the "img" field labeled "Featured Image"
     And I Click the image edit's "New Image" button
    Then I see the "Image" page
     And I see camera is open

#When the user asks to add an image
#Then the camera is opened
#
#When a picture is taken
#Then it is saved to the server
#And listed as one of the available images.
