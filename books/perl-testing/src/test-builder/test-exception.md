# Test::Exception

* Test::Exception

[Test::Exception](https://metacpan.org/pod/Test::Exception).

{% embed include file="src/examples/test-warn/t/test_exception.t" %}

```
1..2
ok 1 - div by 2
ok 2 - div by zero
```

```
throws_ok { $foo->method } 'Error::Simple', 'simple error thrown';
```


Where Error::Simple is the class of the exception that have been thrown. e.g.
by [Exception::Class](https://metacpan.org/pod/Exception::Class).



