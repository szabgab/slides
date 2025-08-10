# Exercise: Implement a TODO list

The main form has an input box and a button. When the user types in some text and clicks on the button,
the back-end stores in in a JSON file. (Dancer provides functions `to_json` and `from_json`.
We can use `Path::Tiny ()` and then `Path::Tiny::path()` with `slurp_utf8` and `spew_utf8`
to read a file and to write it out.




When saving the item we need to save the text the user typed in and an id number. (We can use the `time` function
of `Time::HiRes`.
On the response page list the items we have in the file.


Next to each item add a button with the word "delete" on it.
When clicking on that button, delete the item from the JSON file on the server
and show the list again.






