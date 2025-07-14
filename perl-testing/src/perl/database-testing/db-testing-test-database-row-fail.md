# Test::DatabaseRow fail

{% embed include file="src/examples/db/dbrow_fail.t" %}


The only difference in the test is that we are expecting SZabo instead of Szabo




Results:



```
1..1
not ok 1 - Foo Zorg
#   Failed test 'Foo Zorg'
#   at examples/db/dbrow_fail.t line 15.
# While checking column 'lname' on 1st row
#          got: 'Bar'
#     expected: 'Zorg'
# Looks like you failed 1 test of 1.
```


