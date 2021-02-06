Feature: Calculator

  Scenario: Starting calculator
    Given the calculator app
    Then display is ""

  Scenario: Input one digit
    Given the calculator app
    When clicked on 5
    Then display is "5"

  Scenario: Input more digits
    Given the calculator app
    When clicked on 5
    And clicked on 2
    Then display is "52"

  Scenario: Input digits and operator
    Given the calculator app
    When clicked on 5
    And clicked on 2
    And clicked on +
    Then display is "52+"

  Scenario: First calculation
    Given the calculator app
    When clicked on 5
    And clicked on 2
    And clicked on +
    And clicked on 1
    And clicked on =
    Then display is "53"
    And the history is
      """
      52+1=53
      """

  Scenario: Don't accept letters in the input
    Given the calculator app
    When clicked on <input>
    Then display is ""
    Examples:
     | input |
     |   s   |
     |   a   |
     |   c   |
     |   b   |
     |   !   |

