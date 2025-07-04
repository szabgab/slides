# can_ok('Class', qw(method_a method_b));

* can_ok

can_ok($object, qw(method_a method_b));




In order to nicely test if a module has certain methods you can use the can_ok() function of Test::More.
It can be used both on modules and on objects.

{% embed include file="src/examples/test-perl/t/can_ok.t" %}

Output:


```
1..2
ok 1 - MyTools->can('fibonacci')
not ok 2 - MyTools->can('make_tea')
#   Failed test 'MyTools->can('make_tea')'
#   at examples/test-perl/t/can_ok.t line 11.
#     MyTools->can('make_tea') failed
# Looks like you failed 1 test of 2.
```


