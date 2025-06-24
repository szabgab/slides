# Replace string in Assembly code - using mapping dict

The first imprvement was to create a dictionary with the mapping from old string to new string
and then have a regex that will match exactly the 3 possible original string. In the substitute
part we'll have to use a function as we need the current matching object to access the current match.

The function can be either a `lambda`-expression as in the first solution or a fully defined function
as in the seconde solution that I added only to make it easier to understand the first solution.

This is a nice and working solution, but it has two issues.

In the regex used a character class because we assumed that there are only going to be on-digit registries.
If you look at the original Assembly code you can see there are also R12 and R21.

In addition we now have data duplication. If we change the mapping adding a new original string or removing one,
we'll also have to remember to update the regex. It is not DRY.


{% embed include file="src/examples/regex/assembly_process_dict.py" %}

