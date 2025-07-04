# Fetching a not-existing static page


{% embed include file="src/examples/www/static_bad.t" %}

Fetch a page and check if there is response.

```
$ perl static_bad.t
1..1
not ok 1 - There is a response
#     Failed test (static_bad.t at line 10)
# Looks like you failed 1 tests of 1.
```


