# PHPUnit with assertEqual

Just as was in the case of the SimpleTest, PHPUnit also has an assertEqual method
that allows the separation of the expected value and the actual result.

The first parameter of the assertEqual method is the expected value and the second
parameter is the actual result. Making the roles of the two values clear is
important so in the reporting we can already know what was the expected and what was the
actual result.


{% embed include file="src/examples/php/phpunit/calc03.php" %}

Output

{% embed include file="src/examples/php/phpunit/calc03.php.out" %}

So the difference between this output and the one from
the first example is that in this case the reader can know more
details about the failure. The reader can actually see that the
expected values was 3 while the actual value was 2. That can
already give a clue where the problem might be.





