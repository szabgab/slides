# Exercises: Regular expressions

Pick up a file with some text in it.  (e.g. examples/regex-perl/text.txt ).
Write a script (one for each item) that prints out every line from the file
that matches the requirement.
You can use the script at the end of the page as a starting point but you will
have to change it!



* has a 'q'
* starts with a 'q'
* has 'th'
* has an 'q' or a 'Q'
* has a '*' in it
* starts with an 'q' or an 'Q'
* has both 'a' and 'e' in it
* has an 'a' and somewhere later an 'e'
* does not have an 'a'
* does not have an 'a' nor 'e'
* has an 'a' but not 'e'
* has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
* has at least 3 vowels
* has at least 6 characters
* has at exactly 6 characters
* all the words with either 'Bar' or 'Baz' in them
* all the rows with either 'apple pie' or 'banana pie' in them
* for each row print if it was apple or banana pie?
* Bonus: Print if the same word appears twice in the same line
* Bonus: has a double character (e.g. 'oo')

{% embed include file="src/examples/regex-perl/regex_exercise.pl" %}


