# Manually Patching attribute


We can replace the attribute during the test run and create a json file locally to be used.
At least two problems with this:

* Readers might glance over the assignment and might be baffled
* The change is permanent in the whole test script so one test impacts the other.

{% embed include file="src/examples/exa/test_data_2.py" %}

{% embed include file="src/examples/exa/test_1.json" %}


