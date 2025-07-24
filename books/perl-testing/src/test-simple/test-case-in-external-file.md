# Put the test cases in an external file



By now we almost totally separated the data of the tests in the array from the code that executes the test, but we can go a bit further.

We can move the test data to some external file. Let's create a text file that looks like the following file:

Here each line is a test-case. On the left side of the = sign are the parameters of the sum() function, on the right hand side of the =
is the expected result.

We even allow for empty rows and comments: rows that start with a # character will be disregarded.


{% embed include file="src/examples/test-simple/tests/sum.txt)



Instead of having the data in the BEGIN block, we put code in there that will read the data file line-by-line.
It skips the lines that are either empty or contain only comments.
Lines that contain data are split at every comma and the = sign. Spaces around the signs are removed. The array we get
(@data) contains the information for one test-case. We push the reference to that array on the @tests array.
This way, by the end of the BEGIN block the @tests array will look exactly as it looked in the previous example.

The code outside the BEGIN block stays the same.


{% embed include file="src/examples/test-simple/tests/t24.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t24.pl.out" %}


If for some reason the sum.txt file cannot be opened, we'll get an error message like this:


```
Could not open '.../sum.txt': No such file or directory at t24.pl line 11.
BEGIN failed--compilation aborted at t24.pl line 18.
```


