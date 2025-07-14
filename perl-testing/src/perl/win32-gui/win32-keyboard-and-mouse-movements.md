# Keyboard and mouse movements

* Send keystrokes
* Move the mouse and click on "controls".


* [Win32::GuiTest](https://metacpan.org/pod/Win32::GuiTest)
* [Win32::GUIRobot](https://metacpan.org/pod/Win32::GUIRobot)



Testing command line or networking applications on Microsoft Windows
is the same as testing those applications on Unix or Linux. That does
not need a separate chapter. Especially because Perl will run on MS Windows
as well and nearly all the functionality we have on Unix we also have on
MS Windows.




What is different is the GUI and the way applications interact with each other.
For GUI testing we need to be able to send keystrokes as if someone was typing
at the keyboard and we also need to be able to move the mouse and click on
various objects. In Microsoft terminology the objects are called controls.



Luckily we have the Win32::GuiTest module for our disposal.



