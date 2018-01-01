# Created by jett at 12/25/17
Feature: View Course Email Links
  As a user receiving an invite email
  I want to see what course is planned
  So I can learn what to expect from the course.

  Scenario: Invite Email has Course links - New User
    Given Email with name "New Player Invite" has been received
    When I open the link for "Course Details"
    Then I see the "Five Free Things – Clue Ride" page
    # NOTE: There is an m-dash in the title: ' – '
