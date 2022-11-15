Feature: User can navigate to Mpharma Patient Management Application and create a patient card

  Scenario: User navigates to homepage and creates patient card
    Given Launch chrome browser
    When Open the patient management app homepage
    And enter first name
    And enter middle name
    And enters last name
    And enters phone number
    And enters date of birth
    And enters address
    And clicks on the Add New User button
    Then Patient card is created
    Then close browser
