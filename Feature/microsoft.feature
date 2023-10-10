Feature: Microsoft validation
  Scenario: Catching data google search
    Given User navigates to google
    When I enter qa testing and search
    Then Display the required information
