# Memory leak with cross references

{% embed include file="src/examples/references/memory_leak.pl" %}
{% embed include file="src/examples/references/memory_leak.out" %}



Run the script and when it displays the prompt, check the memory usage.
Passing 100,000 on the command line made it use 39 Mb memory.



