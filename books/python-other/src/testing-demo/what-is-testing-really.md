# What is testing really?

In reality, however, many times we don't get exactly the expected output. Instead there is a small (or big) difference.
That's the bug.

The goal of (automated) testing is to make it easy and cheap to notice when these bugs creep in.

To put it in other words, when you write your code you can check if the result is as expected either manually or by writing
some automated tests. The question, how will you know your piece of code still works half a year from now when someone made
some changes to some other part of the code?

Will you repeate all the manual tests you did earlier? You won't have time for that.

On the other hand if you automated your tests in the first place, then you can easily, quickly and cheaply run them again
and you can verify if everything still works as earlier or if a bug appeared.


* Fixture + Input = Expected Output + Bugs


