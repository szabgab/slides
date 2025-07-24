# Function returning data from bug-tracker



Look at the code that generates the bug reports you'll see that testing the 4th return value
- which is quite complex already - is hard. We cannot test against a fixed hash as some
of the values are totally dynamic (e.g. a timestamp).


{% embed include file="src/examples/test-more/lib/MyBugs.pm" %}



