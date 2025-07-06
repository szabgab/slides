# assetEqual with message

assertEqual can actually get a third parameter too.
This can hold a short description of what is being tested.


{% embed include file="src/examples/php/phpunit/calc04.php" %}

Output



In case of success this does not make a difference but when the
test fails PHPUnit will display this message along with the
name of the test function and the name of the test class.
If the message is worded carefully it can further help in
understanding the failure without even looking at the source code.


{% embed include file="src/examples/php/phpunit/calc04.php.out" %}


