# Solution: count characters

{% embed include file="src/examples/dictionary/count_characters.py" %}

* We need to store the counter somewhere. We could use two lists for that, but that would give a complex solution that runs in O(n**2) time.
* Besides, we are in the chapter about dictionaries so probably we better use a dictionary.
* In the `count` dictionary we each key is going to be one of the characters and the respective value will be the number of times it appeared.
* So if out string is "aabx" then we'll end up with

```
{
    "a": 2,
    "b": 1,
    "x": 1,
}
```

* The `for in` loop on a string will iterate over it character by charter (even if we don't call our variable `char`.
* We check if the current character is a newline `\n` and if it we call `continue` to skip the rest of the iteration. We don't want to count newlines.
* Then we check if we have already seen this character. That is, it is already one of the keys in the `count` dictionary. If not yet, then we add it and put 1 as the values. After all we saw one copy of this character. If we have already seen this character (we get to the `else` part) then we increment the counter for this character.
* We are done now with the data collection.

* In the second loop we go over the keys of the dictionary, that is the characters we have encountered. We sort them in ASCII order.
* Then we print each one of them and the respective value, the number of times the character was found.



