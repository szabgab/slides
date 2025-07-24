Feature: Show the features of Test::BDD::Cucumber
   Run "prove -v  -r --source Feature --ext=.feature ."
   Run pherkin .
   (free text)

Background:
   Given a Fixture called Blue


Scenario: First scenario
    Longer explanation of the scenario (free text)
  Given a Green object
  When I've added "alpha" to the object
  And I've added "beta" to the object
  Then the output is "blabla"
  Then the error is ""


Scenario: Second scenario
    Longer explanation of the scenario (free text)
  Given a Yellow object
  When I've added "gamma" to the object
  And I've added "delta" to the object
  Then the output is "blabla"
  Then the error is "bad, really bad"
