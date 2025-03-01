# How do you know that your code works?

Let's start by looking at this at the individual level. Later we'll see that the same ideas, same principles apply 10-folds when you work in a team and 100 folds if you work in a large
organization, but for now let's focus on you. Let's say you write some software for yourself. Let's make it even more specific. You write a command line tool that takes huge log files
as input, analyzes them, and prints out a report.

How do you know it works correctly?

You'll probably create a small version of the log file where you can manually verify the expected result. You run your program and you check if the result is the same as what you expect.
It does not prove that your code works in all the cases, but this is already much better than if you have never actually checked it manually.

As you feed new copies of the log-file to your program at one point you might encounter a file for which your program crashes. Clearly you did not take account every possible input.
So you dig in the code and the log file, find the source of the problem and fix it. You know that this problem was fixed because you

How do you know that you



At one point you might realize that there are edge cases in the reporting, so you might add 



