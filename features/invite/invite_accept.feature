# Created by jett at 12/29/18
Feature: Accept Invite
  # As an invited new Member with and without a registered device,
  # I would like to accept an invite to play Clue Ride,
  # So that I can join in the fun.

  Scenario: Unregistered with current upcoming Invite
    # This will be the first impression of newly invited Members
    Given Application has been opened
      And I wait for page with "welcome" ID
      And I wait "1" seconds
     When I click the "BDD Mock Register" link
      And I wait for page with "confirm" ID
      And I wait "1" seconds
      And I click the "Use this Email" button
      And I wait "1" seconds
     Then I see the "Invite" page

  Scenario: Registered with current upcoming Invite
    Given Device registered to "invitedUser"
     Then I see the "Invite" page


  Scenario: Registered with declined Invite that I'd like to now accept
    Given Device registered to "declinedUser"
     Then I see the "Invite" page

  Scenario: Registered with Accepted Invite
    Given Device registered to "acceptedInviteUser"
     Then I see the "Home" page

  Scenario: Registered with no outstanding Invites
    # This is what members will see after having played once, but the next
    # Outing hasn't yet been scheduled.
    Given Device registered to "noInviteUser"
     Then I see the "Invite" page

  Scenario: Registered with multiple outstanding Invites
    Given Device registered to "multiInviteUser"
     Then I see the "Invite" page
