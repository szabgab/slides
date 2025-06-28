# Solution: count digits



{% embed include file="src/examples/lists/count_digits.py" %}


First we have to decide where are we going to store the counts. A 10 element long list seems to fit our requirements so if we have 3 0s and 2 8s we would have `[3, 0, 0, 0, 0, 0, 0, 0, 2, 0]`.


* We have a list of numbers.
* We need a place to store the counters. For this we create a variable called counter which is a list of 10 0s. We are going to count the number of times the digit 3 appears in `counters[3]`.
* We iterate over the numbers so `num` is the current number. (e.g. 1203)
* We would like to iterate over the digits in the current number now, but if we write `for var in num` we will get an error `TypeError: 'int' object is not iterable` because `num` is a number, but numbers are not iterables, so we we cannot iterate over them. So we need to convert it to a string using `str`.
* On each iteration `char` will be one character (which in or case we assume that will be a digit, but still stored as a string).
* `int(char)` will convert the string to a number so for example "2" will be converted to 2.
* `count[int(char)]` is going to be `char[2]` if `char` is "2". That's the location in the list where we count how many times the digit 2 appears in our numbers.
* We increment it by one as we have just encountered a new copy of the given digit.
* That finished the data collection.

* The second for-loop iterates over all the "possible digits" that is from 0-9, prints out the digit and the counter in the respective place.




