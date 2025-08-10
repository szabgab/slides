# Silencing the noisy tests

```
make test
```
{% embed include file="src/examples/snippets/noisy_test_output.txt" %}

```
BEGIN {
    $ENV{DANCER_ENVIRONMENT} = 'test';
}
```
{% embed include file="src/examples/snippets/test_output.txt" %}



