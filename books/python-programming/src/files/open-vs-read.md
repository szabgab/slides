# Open vs. Read vs. Load



The expression "open a file" has two distinct meanings for programmers and users of software. For a user of Word, for example,
"open the file" would mean to be able to see its content in a formatted way inside the editor.

When a programmer - now acting as a regular user - opens a Python file in an editor such as Notepad++ or Pycharm,
the expectation is to see the content of that program with nice colors.

However in order to provide this the programmer behind these applications had to do several things.


* Connect to a file on the disk (aka. "opening the file" in programmer speak).
* Read the content of the file from the disk to memory.
* Format the content read from the file as expected by the user of that application.



