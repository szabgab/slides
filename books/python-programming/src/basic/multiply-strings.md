# Multiply string



What if we put the two numbers into quotation marks and this make them strings? Strings that look like number to the naked eyes, but nevertheless
are strings for Python.

If we try to multiply them we get a nasty **exception**. Also known as a **runtime error**. The program stops running.

These exceptions might look nasty, but they are our friends. They tell us what went wrong and exactly where did that happen.

You just need to remember that, at least in Python, you need to read the whole thing from the bottom to top. The last line
holds the error message. Above that you can usually see the content of the line where the problem was found. One line above that
you'll see the name of the file and the line number where the problem occurred.

I strongly urge you to read the error message. If it is not yet clear what is the problem, then copy it to your favorite
search engine and read the explanations you find.

Eventually you'll learn to recognize these messages much faster and it will be much easier to fix the problems.

What this current error message means is we tried to multiply two strings and Python cannot do that.



{% embed include file="src/examples/basics/rectangle_strings.py" %}

**Output:**

{% embed include file="src/examples/basics/rectangle_strings.err" %}



