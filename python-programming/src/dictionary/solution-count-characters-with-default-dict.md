# Solution: count characters with default dict

* collections
* defaultdict


{% embed include file="src/examples/dictionary/count_characters_default_dict.py" %}

* The previous solution can be slightly improved by using `defaultdict` from the `collections` module.
* `count = defaultdict(int)` creates an empty dictionary that has the special feature that if you try to use a key that does not exists, it pretends that it exists and that it has a value 0.
* This allows us to remove the condition checking if the character was already seen and just increment the counter. The first time we encounter a charcter the dictionary will pretend that it was already there with value 0 so everying will work out nicely.



