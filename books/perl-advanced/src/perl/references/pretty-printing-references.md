# Debugging (pretty printing)

* Data::Dumper


But once we have those references we have a better tool to print out their content.

{% embed include file="src/examples/references/dump_content.pl" %}
{% embed include file="src/examples/references/dump_content.out" %}

Actually you can use the Dumper on the references themself without putting them in scalar variables.

```
print Dumper \@names, \%phones;
```



