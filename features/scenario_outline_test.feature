# Created by jett at 10/4/17
Feature: Testing the ability to amend/append to Scenario Outline Examples
  # Enter feature description here

#  Scenario: Here's the Steps
  Scenario Outline: Here's the Steps
    Given I have populated the Examples
    When I have a "<key>", I print a "<value>"
    Examples:
      | key | value |
      | 0   | Starter |

