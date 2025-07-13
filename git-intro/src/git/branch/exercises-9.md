# Exercises Session 9


* Create a file called 'add.sh' with the following content:

{% embed include file="src/examples/git/add.sh" %}

* Make it executable.
* Test it: `./add 23 19` should print 42
* Commit it.

* Create a file called NUMBER and put a 1 in it.
* Commit it.
* Then create 5 more commit changing the file to some other number. (This might help)

```
echo 7 > NUMBER
git commit -am "7"
```

* Then change the `add.sh` file replacing the + by a -.
* Create another 5 commits chaning the NUMBER file.

* No check if the `add.sh` script works
* `./add.sh 23 19` will now prin 4 instead of 42.

* Using bisect find the commit that broke it.


