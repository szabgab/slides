# Without goroutine


Regular functions calls are executed sequentially. Each call can only start after all the previous calls have finished.


{% embed include file="src/examples/without-goroutine/without_goroutine.go" %}
{% embed include file="src/examples/without-goroutine/without_goroutine.out" %}


