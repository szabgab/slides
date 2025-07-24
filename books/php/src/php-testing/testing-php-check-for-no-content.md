# Check for text that should not be there.



In a previous example we checked if the parts of a form are in
place and then immediately we submitted a form with correct values.




We could in fact check a couple of more things. For example we could check
if the "Result" string appears on the page when we access it for the first time
without parameters.




We could also submit the form with missing or bogus data and see how
the application reacts. Especially we can use the assertNoText assertion
to check if a certain text does NOT appear on the page.


{% embed include file="src/examples/php/simpletest/web07.php" %}


This way we can write test for an application without caring how it was written
or in fact in what languages it is written. Once we are reasonably comfortable
with our tests we can start to refactor the application.




