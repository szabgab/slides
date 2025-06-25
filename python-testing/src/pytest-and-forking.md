# Pytest and forking

* This tests passes and generates two reports.
* I could not find a way yet to avoid the reporting in the child-process. Maybe we need to run this with a special runner that will fork and run this test on  our behalf.


{% embed include file="src/examples/pytest/fork/app.py" %}
{% embed include file="src/examples/pytest/fork/test_app.py" %}

{% embed include file="src/examples/pytest/cases/test_one.py" %}


