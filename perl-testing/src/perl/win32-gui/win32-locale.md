# Locale

* setlocale
* LC_CTYPE


The current locale is what tells the application in what language it should
display its strings. We use this information in an external file to
find out what strings to expect.


This script gets a parameter --app with a value 'calculator' or 'notepad' or 'notepad_menu' just
to be able to return the appropriate strings in the current language. For example:
`perl locale.pl --app calculator`


TODO: include: examples/Win32GUI/locale.pl



