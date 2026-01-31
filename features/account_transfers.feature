Feature: Personal account transfers

  Scenario: Incoming transfer increases balance
    Given A personal account is created with balance 1000
    When An incoming transfer of "500" received
    Then The balance should be 1500

  Scenario: Outgoing transfer decreases balance
    Given A personal account is created with balance 1000
    When An outgoing transfer of 300 sent
    Then The balance should be 700

  Scenario: Outgoing transfer fails if insufficient balance
    Given A personal account is created with balance 200
    When An outgoing transfer of 300 sent
    Then The balance should be 200

  Scenario: Express outgoing transfer ignores balance limit
    Given A personal account is created with balance 200
    When An express outgoing transfer of 200 sent
    Then The balance should be -1
