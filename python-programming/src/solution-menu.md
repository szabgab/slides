# Solution: menu

{% embed include file="src/examples/lists/colors.py" %}

* We would like to show a menu where each number corresponds to one element of the list so this is one of the places where we need to iterate over the indexes of a list.
* `len(colors)` gives us the length of the list (in our case 4)
* `range(len(colors))` is the range of numbers between 0 and 4 (in our case), meaning 0, 1, 2, 3.
* (Sometimes people explicitly write 4 in this solution, but if later we change the list and include another color we'll have to remember updating this number as well. This is error prone and it is very easy to deduct this number from the data we already have. (The list.))
* We start the list from 0, but when we display the menu we would like to show the numbers 1-4 to make it more human friendly. Therefore we show `ix+1` and the color from locations `ix`.
* We ask for input and save it in a variable.

* We use the `isdecimal` method to check if the user typed in a decimal number. We give an error and exit if not.
* Then we check if the users provided a number in the correct range of values. We give an error and exit if not.
* then we convert the value to the correct range of numbers (remember, the user sees and selects numbers between 1-4 and we need them between 0-3).



