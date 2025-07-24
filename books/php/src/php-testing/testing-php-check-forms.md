# Checking forms

To further check if the page is correct we could check,
using assertField(), if the form we expect to be on the
page has the input fields as we expect them. We can even
check if they have the correct preset values.


{% embed include file="src/examples/php/simpletest/web05.php" %}


Unfortunately due to external limitations currently this code
cannot recognize if there are more than one forms on the page
and will mash them together for our purposes.




