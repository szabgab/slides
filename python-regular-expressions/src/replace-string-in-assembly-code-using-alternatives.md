# Replace string in Assembly code - using alternatives

We can solve the first issue by changing the regex. Instead of using a character class, we use alternatives (vertical line, aka. pipe)
and fully write down the original strings.

The rest of the code is the same and the second issue is not solved yet, we still have to make sure the keys of the dictionary and the values
in the regex are the same.

However this solution makes it easier to solve the second issue as well.

{% embed include file="src/examples/regex/assembly_process_dict2.py" %}


