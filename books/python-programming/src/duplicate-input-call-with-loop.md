# Duplicate input call with loop


* A `while` loop would be a better solution.
* This works, but now we have duplicated the `input` call and the text is different in the two cases. [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
* We can't remove the first call of `input` as we need the `id_str` variable in the condition of the `while` already.

{% embed include file="src/examples/loops/duplicate_input_call.py" %}



