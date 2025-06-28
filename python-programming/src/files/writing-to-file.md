# Writing to file

* open
* write


In order to write to a file we open it passing the "w" write mode. If the file did not exist it will try to create it.
If the file already existed it will remove all its content so after such call to `open` we'll end up with an empty
file if we don't write into it.

Once the file is opened we can use the `write` method to write to it. This will NOT automatically append a newline
at the end so we'll have to include `\n` if we would like to insert a newline.

Opening the file will fail if we don't have write permissions or if the folder in which we are trying to create the
file does not exist.



{% embed include file="src/examples/files/write.py" %}


