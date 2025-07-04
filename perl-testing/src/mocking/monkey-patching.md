# Monkey Patching


{% embed include file="src/examples/mock/Monkey.pm" %}
{% embed include file="src/examples/mock/check_monkey.t" %}

```
1..4
ok 1 - bananas
ok 2 - is_hungry
not ok 3 - bananas
#   Failed test 'bananas'
#   at check_monkey.t line 13.
#          got: '9'
#     expected: '10'
not ok 4 - bananas
#   Failed test 'bananas'
#   at check_monkey.t line 15.
#          got: '8'
#     expected: '9'
# Looks like you failed 2 tests of 4.
```
{% embed include file="src/examples/mock/patch_monkey.t" %}

```
1..5
ok 1 - bananas
ok 2 - is_hungry
ok 3 - eat called
ok 4 - bananas
ok 5 - bananas
```


