# GUI with Python/Tk
{id: tk}

## Sample Tk Demo app
{id: tk-simple}

{aside}
This application shows a number of widgets available in Python Tk.
The primary goal is to show a few features that we'll learn about on the following pages.
{/aside}

* On recent versions of Ubuntu you might need to install python3-tk in addition to python3 using

```
sudo apt-get install python3-tk
```

![](examples/tk/tk_demo.py)

## Simple file dialog
{id: simple-file-dialog}
{i: filedialog}
{i: askopenfilename}

{aside}
This is another way of using the Tk widgets. Here we have a plain command-line script, but instead of using the
standard `input()` function of Python to ask for a filename it launches a Tk File-dialog widget to allow the user to browse
and select a file.
{/aside}

![](examples/tk/simple_file_dialog.py)


## GUI Toolkits
{id: gui-toolkits}
{i: Tk}
{i: GTK}
{i: Qt}
{i: wxWidgets}
{i: GUI}

{aside}
When creating an application there are several ways to interact with the user. You can accept command line parameters.
You can interact on the Standard Output / Standard Input runnin in a Unix Shell or in the Command Prompt of Windows.

Many people, especially those who are using MS Windows, will frown upon both of those. They expect a Graphical User Interface (GUI)
or maybe a web interface via their browser. In this chapter we are going to look at the possibility to create a desktop GUI.


There are plenty of ways to create a GUI in Python. The major ones were listed here, but there are many more. See the additional links.

In this chapter we are going to use the Tk Toolkit.
{/aside}

* [Tk](https://docs.python.org/library/tk.html)
* [GTK](http://www.pygtk.org/)
* [Qt](https://wiki.python.org/moin/PyQt)
* [wxWidgets](http://wxpython.org/)

* [GUI FAQ](https://docs.python.org/faq/gui.html)
* [GUI Programming](https://wiki.python.org/moin/GuiProgramming)

## Installation
{id: tcltk-installation}

{aside}
Tk in Python is actually a wrapper arount the implementation in Tcl.

Tcl/Tk usually comes installed with Python. All we need is basically the Tkinter Python module.
In some Python installations (e.g. Anaconda), Tkinter is already installed. In other cases you might
need to install it yourself. For examples on Ubuntu you can use `apt` to install it.
{/aside}

```
sudo apt-get install python3-tk

pip install tk
```

## Python Tk Documentation
{id: tk-documentation}

{aside}
The documentation of Tk in Python does not cover all the aspects of Tk. If you are creating a complex GUI
application you might need to dig in the documentation written for Tcl/Tk.
{/aside}

* [Tk](https://docs.python.org/library/tk.html)
* The [Tk Command](https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm) of [Tcl 8.6](https://www.tcl.tk/man/tcl8.6/)
* [Python GUI Geeks for Geeks](https://www.geeksforgeeks.org/python-gui-tkinter/)


{aside}
In the Unix world where Tk came from the various parts of a GUI application are called widgets. In the MS Windows world
they are usually called controls. There are several commonly used Widgets. For example, Label, Button, Entry, Radiobutton, Checkbox.
First we are going to see small examples with each one of these Widgets. Then we'll see how to combine them.
{/aside}

## Python Tk Button
{id: tk-button}
{i: Button}

* [Button](https://effbot.org/tkinterbook/button.htm)

![](examples/tk/tk_button.py)

## Python Tk Button with action
{id: tk-button-with-action}

![](examples/tk/tk_button_with_action.py)


## Python Tk Label
{id: tk-label}
{i: tkinter}
{i: Tk}
{i: Label}
{i: pack}
{i: mainloop}

* [Label](https://effbot.org/tkinterbook/label.htm)

![](examples/tk/tk_label.py)


## Python Tk Label - font size and color
{id: tk-label-font}
{i: config}
{i: color}
{i: font}

![](examples/tk/tk_label_font.py)

## Python Tk echo - change text of label
{id: tk-echo}
{i: Entry}
{i: Label}
{i: Button}

* Entry window, Button, Label where to show the text we typed in.

![](examples/tk/tk_echo.py)


## Python Tk Keybinding
{id: tk-keybinding}
{i: bind}

![](examples/tk/tk_key_binding.py)

* Alt-F4 is already bound to exit

## Python Tk Mouse clicks
{id: tk-mouse-clicks}

![](examples/tk/tk_mouse_clicks.py)

## Python Tk Mouse movements (motions)
{id: tk-mouse-movements}

![](examples/tk/tk_mouse_motion.py)

## Python Tk Entry (one-line text entry)
{id: tk-entry}
{i: Entry}

* [Entry](https://effbot.org/tkinterbook/entry.htm)

![](examples/tk/tk_entry.py)


## Python Tk Entry for passwords and other secrets (hidden text)
{id: tk-entry-passwords}

![](examples/tk/tk_entry_secret.py)


## Python Tk Checkbox
{id: tk-checkbox}
{i: Checkbox}
{i: BooleanVar}

![](examples/tk/tk_checkbox.py)

* [Variables](https://docs.python.org/library/tkinter.html#coupling-widget-variables)


## Python Tk Radiobutton
{id: tk-radiobutton}
{i: Radiobutton}

![](examples/tk/tk_radiobutton.py)


## Python Tk Listbox
{id: tk-listbox}
{i: Listbox}
{i: END}
{i: curselection}
{i: get}

![](examples/tk/tk_listbox.py)


## Python Tk Listbox Multiple
{id: tk-listbox-multiple}
{i: selectmode}
{i: MULTIPLE}

![](examples/tk/tk_listbox_more.py)

## Python Tk Menubar
{id: tk-menubar}
{i: Menu}
{i: add_cascade}
{i: add_command}

* [Menubar](http://effbot.org/zone/tkinter-menubar.htm)
* [Menu](http://effbot.org/tkinterbook/menu.htm)

* `underline` sets the hot-key.
* `tearoff=` (the default) allows floating menu by clicking on the dashed line.
* enable/disable menu items.
* Set actions via `command` on the menu items.

![](examples/tk/tk_menu.py)


## Python Tk Text
{id: tk-text}
{i: Text}

![](examples/tk/tk_text.py)

* `text.delete(1.0, tk.END)`
* `text.insert('end', content)`
* `content = text.get(1.0, tk.END)`

* [tk text](http://effbot.org/tkinterbook/text.htm)


## Python Tk Dialogs
{id: tk-dialogs}

* [Dialogs](https://docs.python.org/library/dialog.html)
* Simple dialogs
* Filedialogs
* Message boxes

## Python Tk simple dialog to get a single string, int, or float
{id: tk-simpledialog}

![](examples/tk/tk_simple_dialog.py)


## Python Tk Filedialog
{id: tk-filedialog}
{i: filedialog}
{i: askopenfilename}
{i: asksaveasfilename}
{i: askopenfile}
{i: asksaveasfile}

* [file dialogs](http://effbot.org/tkinterbook/tkinter-file-dialogs.htm)
* [dialog](https://docs.python.org/library/dialog.html)

* askopenfilename - returns path to file
* asksaveasfilename - returns path to file
* askopenfile - returns filehandle opened for reading
* asksaveasfile - retutns filehandle opened for writing

* Allow the listing of file-extension filters.

![](examples/tk/tk_filedialog.py)


## Python Tk messagebox
{id: tk-messagebox}

![](examples/tk/tk_messagebox.py)

* [Tk messagebox](https://docs.python.org/library/tkinter.messagebox.html)

## Python Tk - custom simple dialog with its own widgets and buttons
{id: tk-customized-simple-dialog}

![](examples/tk/tk_custom_simple_dialog.py)



## Python Tk Combobox
{id: tk-combobox}
{i: Combobox}
{i: ComboboxSelected}
{i: bind}

![](examples/tk/tk_combobox.py)

## Python Tk OptionMenu
{id: tk-optionmenu}
{i: OptionMenu}
{i: StringVar}

![](examples/tk/tk_optionmenu.py)


## Python Tk Scale
{id: tk-scale}
{i: Scale}
{i: HORIZONTAL}
{i: VERTICAL}

![](examples/tk/tk_scale.py)


## Python Tk Progressbar
{id: tk-progressbar}
{i: Progreessbar}

![](examples/tk/tk_progressbar.py)


## Python Tk Frame
{id: tk-frame}
{i: Frame}
{i: pack}
{i: side}

![](examples/tk/tk_frame.py)

* width
* side: left, right, top, bottom

## Python Tk display images using Canvas
{id: python-tk-display-images}

![](examples/tk/tk_image.py)
![](examples/tk/tk_images.py)

## Python Tk display Hebrew text (right to left)
{id: python-tk-hebrew-text}

![](examples/tk/tk_hebrew.py)

## Python Tk Colorchooser
{id: tk-colorchooser}

* [colorchooser](https://docs.python.org/library/tkinter.colorchooser.html)

![](examples/tk/tk_colorchooser.py)

## Python Tk Timer event (after)
{id: tk-timer-event}
{i: after}

{aside}
Schedule an event to be execute `after` N miliseconds.
{/aside}

![](examples/tk/tk_timer.py)

## Python Tk Class-based Label + Button
{id: tk-class-based-label-button}

![](examples/tk/tk_class_button.py)

## Tk: Runner
{id: tk-runner}
{i: Button}
{i: Text}

![](examples/tk/tk_runner.py)

## Tk: Runner with threads
{id: tk-runner-with-threads}
{i: threading}
{i: queue}
{i: ctypes}

![](examples/tk/tk_runner_threads.py)


## Tk: Old Simple Tk app with class
{id: tk-simple-class}
{i: tkinter}
{i: Tk}
{i: mainloop}
{i: Frame}

![](examples/tk/simple.py)


## Tk: Old Hello World
{id: tk-hello-world}
{i: Label}

![](examples/tk/hello_world.py)


## Tk: Old Quit button
{id: tk-quit-button}
{i: Button}

![](examples/tk/quit.py)


## Tk: Old File selector
{id: tk-file-selector}
{i: Entry}
{i: filedialog}

![](examples/tk/file_selector.py)

## Tk: Old Checkbox
{id: tk-checkbox2}
{i: Checkbutton}

![](examples/tk/tk_checkbox_complex.py)

## Tk: Old Getting started with Tk
{id: getting-started-with-tk}
{i: Tk}

![](examples/tk/tk_example.py)

## Exercise: Tk - Calculator one line
{id: exercise-tk-calculator-one-line}

Write a Tk application that behaves like a one-line calculator.
It has an entry box where one can enter an expression like "2 + 3" and a button.
When the button is pressed the expression is calculated.

There is another button called "Quit" that will close the application.

## Exercise: Tk - Calculator with buttons
{id: exercise-tk-calculator-with-button}

* This is a Calculator app that already has buttons for the digits 0-9
* Buttons for the operators `+-*/`
* A button for `=`
* A window where we can see what we type in using the buttons or using the keyboard.

## Exercise: Tk - Convert between CSV and Excel files
{id: exercise-tk-convert-csv-file}

* Write a Tk-based application that can convert CSV to Excel and Excel to CSV.

* Select an existing .csv file or .xlsx file
* Select a filename for output
* Click a button to convert
* Have a place for messages or use pop-up message windows.


## Exercise: Tk - Shopping list
{id: exercise-tk-shopping-list}

Create a Tk application that allows you to create a [shopping list](https://code-maven.com/shopping-list).


## Exercise: Tk - TODO list
{id: exercise-tk-todo-list}

* Create a Tk application to handle your TODO items.
* A Menu to be able to exit the application
* A List of current tasks.
* A way to add a new task. For a start each task has a title and a status. The status can be "todo" or "done". (default is "todo")
* A way to edit a task. (Primarily to change its title).
* A way to mark an item as "done" or mark it as "todo".
* A way to move items up and down in the list.
* The application should automatically save the items in their most up-to-date state in a "database". The database can be a JSON file or and SQLite database or anything else you feel fit.


## Exercise: Tk - Notepad
{id: exercise-tk-notepad}

* Create a Notepad like text editor.
* It needs to have a menu called File with item: New/Open/Save/Save As/Exit
* It needs to have an area where it can show the content of a file. Let you edit it.

* Create a menu called About that displays an about box containing the names of the authors of the app.
* Menu item to Search for text.

## Exercise: Tk - Copy files
{id: exercise-tk-copy-files}

An application that allows you to type in, or select an existing file and another filename
for which the file does not exists.
Then copy the old file to the new name.

## Exercise: Tk - Implement Master Mind board
{id: exercise-tk-master-mind}

Create an application that we can use to play [Master Mind](https://en.wikipedia.org/wiki/Mastermind_(board_game))

## Exercise: Tk - a GUI for a grep-like application
{id: exercise-tk-grep}

The GUI should accept:

* A filename, a wilde-card expression, maybe a dirctory name (and then a flag to recurse or not).
* A regular expression.
* Various flags for regex.

* Then it should display the lines that match the expression in the selected files.

## Solution: Tk - Calculator one line
{id: solution-tk-calcilator-one-line}
{i: Entry}
{i: delete}
{i: insert}

![](examples/tk/calculator_one_line.py)

## Solution: Tk - Calculator with buttons
{id: solution-tk-calculator-with-button}
{i: Button}

![](examples/tk/calculator_with_buttons.py)

## Solution: Tk - Convert between CSV and Excel files
{id: solution-tk-convert-csv-file}

![](examples/tk/convert_file.py)


## Solution: Tk - Implement Master Mind board
{id: solution-tk-master-mind}

TBD

## Solution: Tk - Notepad
{id: solution-tk-notepad}

![](examples/tk/tk_notepad.py)


