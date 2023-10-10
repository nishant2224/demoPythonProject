Feature: Flipkart Validation
  Scenario: Search for Apple in Flipkart
    Given User navigates to flipkart
    When User closes the login popup
    When I enter "Apple" into search
    Then Display the first gadget that appears


