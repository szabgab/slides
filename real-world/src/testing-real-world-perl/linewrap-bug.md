# Linewrap bug

{% embed include file="src/examples/mocking-functions/linewrap_snippet.t" %}

```
1..4
ok 1
ok 2
ok 3
not ok 4
#   Failed test at linewrap.t line 46.
#     Structures begin differing at:
#          $got->{Miley Cyrus} = '1'
#     $expected->{Miley Cyrus} = '2'
# Looks like you failed 1 test of 4.
```


