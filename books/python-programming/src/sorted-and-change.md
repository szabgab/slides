# Sorted and change - shallow copy


* Sorted creates a shallow copy of the original list

* If the list elements are simple values that creates a copy

{% embed include file="src/examples/lists/sorted_and_change.py" %}

**Output:**

{% embed include file="src/examples/lists/sorted_and_change.out" %}

* If some of the elements are complex structures (list, dictionaries, etc.) then the internal structures are not copied.
* One can use `copy.deepcopy` to make sure the whole structure is separated, if that's needed.

{% embed include file="src/examples/lists/sorted_and_change_deep.py" %}

**Output:**

{% embed include file="src/examples/lists/sorted_and_change_deep.out" %}


