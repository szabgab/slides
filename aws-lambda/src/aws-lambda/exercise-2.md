# Exercise 2


* Fix the Python code so even if the user does not supply the "name" field it still won't crash.
* Instead make it return a JSON structure with status "400 Bad Request"
* Use `curl -I` or `curl -D err.txt` to check the headers as well.

* Create another function that will accept 2 numbers (parameters a and b) and add them together returning a JSON that looks like this:

```
{
   'a' : 23,
   'b' : 19,
   'op' : '+'
   'result' : 42
}
```


