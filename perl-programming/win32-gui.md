# Microsoft Windows GUI Testing
{id: win32-gui}

## GUI testing
{id: manual-gui-testing}

* Launch the application
* Find various controls
* Type in values/check if they show up correctly
* Push buttons
* Check if results are correct

We cannot separate testing from development. We cannot say that after the developers
have written something we can test everything as black box, no matter how they developed it.


## Keyboard and mouse movements
{id: win32-keyboard-and-mouse-movements}

* Send keystrokes
* Move the mouse and click on "controls".


* [Win32::GuiTest](https://metacpan.org/pod/Win32::GuiTest)
* [Win32::GUIRobot](https://metacpan.org/pod/Win32::GUIRobot)


{aside}
Testing command line or networking applications on Microsoft Windows
is the same as testing those applications on Unix or Linux. That does
not need a separate chapter. Especially because Perl will run on MS Windows
as well and nearly all the functionality we have on Unix we also have on
MS Windows.
{/aside}


{aside}
What is different is the GUI and the way applications interact with each other.
For GUI testing we need to be able to send keystrokes as if someone was typing
at the keyboard and we also need to be able to move the mouse and click on
various objects. In Microsoft terminology the objects are called controls.
{/aside}

{aside}
Luckily we have the Win32::GuiTest module for our disposal.
{/aside}


## Win32::GuiTest
{id: win32-guitest}
{i: Win32::GuiTest}

* Written and maintained by Ernesto Guisado Jarek Jurasz and others.
* Now maintained by Dmitry Karasik.
* Available since 1998.



## Win32::GUIRobot
{id: win32-guirobot}
{i: Win32::GUIRobot}

* Written by Dmitry Karasik.
* Available since 2007.



## Calculator
{id: win32-calculator}

```
calc.exe

perl calc.pl
```

```
Testing a calculator might be simple. This is the reason we use this example.
```


## Launch the application
{id: win32-launch-application}
{i: start}
{i: :ALL}
{i: FindWindowLike}

```
Launch the application and find the id of the new window
Make sure there is exactly one such application running
Run the code twice without closing the window and see the error message.

Use the start command in order to detach the calc.exe from our Perl
script and both will be able to run simultaneously.
```
![](examples/Win32GUI/calc01.pl)



## Locale
{id: win32-locale}
{i: setlocale}
{i: LC_CTYPE}


The current locale is what tells the application in what language it should
display its strings. We use this information in an external file to
find out what strings to expect.


This script gets a parameter --app with a value 'calculator' or 'notepad' or 'notepad_menu' just
to be able to return the appropriate strings in the current language. For example:
`perl locale.pl --app calculator`


TODO: include: examples/Win32GUI/locale.pl


## Close the application
{id: win32-close-the-application}
{i: Alt-F4}
{i: SendKeys}
{i: %{F4}}

```
Close the application by Alt-F4

% means Alt
{F4} means the F4 key.
```
![](examples/Win32GUI/calc02.pl)


## Using the Keyboard
{id: win32-using-the-keyboard}
{i: PushButton}
![](examples/Win32GUI/calc03.pl)

```
Type in the calculation and see as the calculator reaches the result.
Nice. It would be even better if after we typed in the values and pressed =
we would be able to read the result automatically and then compare it to
our expected value.
```


## Check the children
{id: win32-check-child-windows}
{i: GetChildWindows}
{i: GetWindowText}
![](examples/Win32GUI/calc04.pl)

```
Check out the children, Try to find the window where the results should be
It does not have a text and there are 3 such controls - without a name
```


## Fetch content of a control
{id: win32-fetch-content-of-control}
{i: WMGetText}
![](examples/Win32GUI/calc05.pl)


Catch the content of the first child.
At this point we can only hope that this is the child that holds the result
as it does not have a title, maybe it has a type that we can check ?
Or maybe it is time to ask the engineers to give a title to this control ?




## Window location
{id: win32-window-location}
{i: GetWindowRect}
![](examples/Win32GUI/calc11.pl)

{aside}

As we would like to start to use the mouse now, first we should find out where are,
we and where is the window?
{/aside}

{aside}

Check the location of the windows.
Run this script several times and see the data.
As we can see all 4 values change so while the first two are x and y coordinates of
the top left corner the other two values are not width and height. Looking at the data
more closely we can see that the two other values are the coordinates of the bottom right
corner.
{/aside}



## Move the mouse
{id: win32-move-the-mouse}
{i: MouseMoveAbsPix}
![](examples/Win32GUI/calc12.pl)


Let's try to move the mouse to the top left corner.
Here we can see that the location of the mouse is at the outside
of the window heading.




## Move the cursor around the edges
{id: win32-move-cursor}
![](examples/Win32GUI/calc13.pl)


And now we would like to see that we can draw the outline of the windows
with our mouse




## Close the window by a mouse click
{id: win32-close-window-by-mouse}
{i: SendMouse}
{i: {LeftClick}}
![](examples/Win32GUI/calc14.pl)


Now that we know how to move the mouse we can even use it to click on the
x in the top right corner exiting the application with a mouse click.




## Calculate using the mouse
{id: win32-calculate-using-mouse}
![](examples/Win32GUI/calc15.pl)

```
Now we could calculate the location of the various buttons based
on the size of the window and our feeling about the size but
we remember that most of the children of the main Calculator window
had a name, so it will be quite easy to find them.
```



## The full calc.pl example
{id: win32-full-calc-example}
![](examples/Win32GUI/calc.pl)


## Installing Win32::GuiTest
{id: download-win32-guitest}


The latest version is <a href="http://metacpan.org/pod/Win32::GuiTest">on CPAN</a>




## Tools
{id: win32-tools}

* Windows spy (probably defunct)
* Winspector (?)
* Spy++ that comes with Visual Studio
* [WinExplorer](http://www.nirsoft.net/utils/winexp.html)
* [Win32::GuiTest](http://metacpan.org/pod/Win32::GuiTest)
* [Win32::GUIRobot](http://metacpan.org/pod/Win32::GUIRobot)
* spy.pl that comes with Win32::GuiTest, but is also included here

![](examples/Win32GUI/spy.pl)




