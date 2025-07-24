# do-while loop in JavaScript

* do while

The loop is executed at least once.

{% embed include file="src/examples/js/do_while.js" %}

For example you ask a question and let the user guess. Every time you compare
the answer to the expected answer. You will need to
get the value from the user before the first compare, and then if it fails,
ask the user again. If you use plain "while" then you'll have to read from the user
once before the while-loop and then inside the loop too. OTOH if you use the "do-while"
loop, it is enought to ask in the do-block.


