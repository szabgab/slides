# File types: Text vs Binary



You probably know many file types such as Images (png, jpg, ...), Word, Excel, mp3, mp4, csv, and now also .py files. Internally there are two big categories.
Text and Binary files. Text files are the ones that look readable if you open them with a plain text editor such as Notepad. Binary files will
look like a mess if you opened them in Noetpad.

For Binary files you need a special application to "look" at their content. For example
the Excel and Word programs for the appropriate files. Some image viewer application to view all the images.
VLC to look at an mp4. Some application to hear the content of mp3 files.


* Text: Can make sense when opened with Notepad: .txt, csv, .py, .pl, ..., HTML , XML, YAML, JSON
* Binary: Need specialized tool to make sense of it: Images, Zip files, Word, Excel, .exe, mp3, mp4


In Python you have specialized modules for each well-knonw binary type to handle the files of that format. Text files on the other
hand can be handled by low level file-reading functions, however even for those we usually have modules that know how to read
and interpret the specific formats. (e.g. CSV, HTML, XML, YAML, JSON parsers)


