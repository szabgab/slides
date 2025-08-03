# Converting string to integer - strconv, Atoi

* strconv
* Atoi
* err
* nil

{% embed include file="src/examples/convert-string-to-integer/convert_string_to_integer.go" %}
{% embed include file="src/examples/convert-string-to-integer/convert_string_to_integer.out" %}

* In the first two examples the conversion was successful.
* In the 3rd and 4th examples it failed.
* How can we know?


While internally Go can represent numbers, the communication with the outside world is always using strings. So when we read from a file we always get strings. When we ask the user to type in a number and the user types in a number, we still receive it as a string.
For example as the string `"42"`. So we need a way to convert a string that looks like a number to the numeric representation of Go.




