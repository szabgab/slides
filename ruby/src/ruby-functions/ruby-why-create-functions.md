# Why create functions?

* Code reuse
* Easier organization of the code
* Less things to keep in mind at once
* Easier maintenance
* Easier testing


Before we get into how to create and use function, let's talk a bit about why you'd want to create them?

There are several reasonse mentioned here.

One of the is code reuse. It is much better to create a function and use it in several places in your code than to copy
and paste the same several lines. For one it will mean you have less code to maintain. Consider this:

You wrote some code to do some work. You need it in several places. So you copy the code. Then a month later you find a bug in one of these copies and fix it.
Will you remember to go to all the other copies and fix it there too or will you wait till someone uses that part of the application and encounters the bug?

However, let's be positive positive and instead of a bug what will happen if you find a way to do the same job 10 times faster? Will you now go and replace all the copies?

If you had the code in a function then you only need to fix the bug or update to the faster version in one place and you get the impact everywhere.



