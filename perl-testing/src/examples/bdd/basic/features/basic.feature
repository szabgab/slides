Feature: Hello World

  Scenario: Hello World
    Given the HelloWorld module
    When calling hello_world function
    Then return is "Hello World!"
