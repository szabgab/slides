# GUI with Python/Tk
{id: tk}

## Sample Tk app
{id: tk-simple}

![](examples/tk/tk_demo.py)


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

* [GUI FAQ](https://docs.python.org/3/faq/gui.html)
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


## Python Tk Keybinding
{id: tk-keybinding}
{i: bind}

![](examples/tk/tk_key_binding.py)


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

* [Variables](https://docs.python.org/3.9/library/tkinter.html#coupling-widget-variables)


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
* Filedialogs
* Message boxes


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


## Not so Simple Tk app with class
{id: tk-simple-class}
{i: tkinter}
{i: Tk}
{i: mainloop}
{i: Frame}

![](examples/tk/simple.py)


## Tk: Hello World
{id: tk-hello-world}
{i: Label}

![](examples/tk/hello_world.py)


## Tk: Quit button
{id: tk-quit-button}
{i: Button}

![](examples/tk/quit.py)


## Tk: File selector
{id: tk-file-selector}
{i: Entry}
{i: filedialog}

![](examples/tk/file_selector.py)

## Tk: Checkbox
{id: tk-checkbox2}
{i: Checkbutton}

![](examples/tk/tk_checkbox_complex.py)

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

## Getting started with Tk
{id: getting-started-with-tk}
{i: Tk}

![](examples/tk/tk_example.py)


## Exercise: Tk - Calculator one line
{id: exercise-tk-calculator-one-line}

Write a Tk application that behaves like a one-line calculator.
It has an entry box where one can enter an expression like "2 + 3" and a button.
When the button is pressed the expression is calculated.

There is another button called "Quit" that will close the application.

## Exercise: Tk Shopping list
{id: exercise-tk-shopping-list}

Create a Tk application that allows you to create a [shopping list](https://code-maven.com/shopping-list).


## Exercise: Tk TODO list
{id: exercise-tk-todo-list}

* Create a Tk application to handle your TODO items.
* A Menu to be able to exit the application
* A List of current tasks.
* A way to add a new task. For a start each task has a title and a status. The status can be "todo" or "done". (default is "todo")
* A way to edit a task. (Primarily to change its title).
* A way to mark an item as "done" or mark it as "todo".
* A way to move items up and down in the list.
* The application should automatically save the items in their most up-to-date state in a "database". The database can be a JSON file or and SQLite database or anything else you feel fit.


## Exercise: Tk Notepad
{id: exercise-tk-notepad}

* Create a Notepad like text editor.
* It needs to have a menu called File with item: New/Open/Save/Save As/Exit
* It needs to have an area where it can show the content of a file. Let you edit it.

* Create a menu called About that displays an about box containing the names of the authors of the app.
* Menu item to Search for text.

## Exercise: Tk Copy files
{id: exercise-tk-copy-files}

An application that allows you to type in, or select an existing file and another filename
for which the file does not exists.
Then copy the old file to the new name.

## Exercise: Tk
{id: exercise-tk}

* Application that accepts a "title" - line of text, a file selected, a new filename (that probably does not exist) and then runs.

## Solution: Tk - Calculator one line
{id: solution-tk-calcilator-one-line}
{i: Entry}
{i: delete}
{i: insert}
{i: Button}

![](examples/tk/calculator_one_line.py)

![](examples/tk/calculator.py)


## Solution: Tk
{id: solution-tk}

![](examples/tk/convert_file.py)

## Solution: Tk Notepad
{id: solution-tk-notepad}

![](examples/tk/tk_notepad.py)

