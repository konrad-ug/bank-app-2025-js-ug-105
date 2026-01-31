Feature: Account registry

Scenario: User is able to create 2 accounts
    Given Account registry is empty
    When I create an account using first_name: "kurt", last_name: "cobain", pesel: "89092909246", email: "email@email.pl"
    And I create an account using first_name: "tadeusz", last_name: "szcześniak", pesel: "79101011234", email: "email@email.pl"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "89092909246" exists in registry
    And Account with pesel "79101011234" exists in registry

Scenario: User is able to update surname of already created account
    Given Account registry is empty
    And I create an account using first_name: "nata", last_name: "haydamaky", pesel: "95092909876", email: "email@email.pl"
    When I update "last_name" of account with pesel: "95092909876" to "filatov"
    Then Account with pesel "95092909876" has "last_name" equal to "filatov"

Scenario: User is able to update name of already created account
    Given Account registry is empty
    And I create an account using first_name: "Jan", last_name: "Kowalski", pesel: "12345678901", email: "email@email.pl"
    When I update "first_name" of account with pesel: "12345678901" to "Marcin"
    Then Account with pesel "12345678901" has "first_name" equal to "Marcin"

Scenario: Created account has all fields correctly set
    Given Account registry is empty
    And I create an account using first_name: "Anna", last_name: "Nowak", pesel: "02322002853", email: "email@email.pl"
    Then Account with pesel "02322002853" has "first_name" equal to "Anna"
    And Account with pesel "02322002853" has "last_name" equal to "Nowak"
    And Account with pesel "02322002853" has "pesel" equal to "02322002853"
    And Account with pesel "02322002853" has "email" equal to "email@email.pl"

Scenario: User is able to delete created account
    Given Account registry is empty
    And I create an account using first_name: "parov", last_name: "stelar", pesel: "01092909876", email: "email@email.pl"
    When I delete account with pesel: "01092909876"
    Then Account with pesel "01092909876" does not exist in registry
    And Number of accounts in registry equals: "0"