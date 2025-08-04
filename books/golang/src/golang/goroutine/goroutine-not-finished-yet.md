# goroutine not finished yet

* go


In this example we told the first call to run 30 times, but it could only run 6 times before the main part of the code finished that killed the whole process. So we need to be able to wait till the go-routine finishes.


{% embed include file="src/examples/goroutine-not-finished-yet/goroutine_not_finished_yet.go" %}
{% embed include file="src/examples/goroutine-not-finished-yet/goroutine_not_finished_yet.out" %}


