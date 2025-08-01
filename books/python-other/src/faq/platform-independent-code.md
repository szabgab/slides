# Platform independent code

In general Python is platform independent, but still needs some care to make sure
you don't step on some aspects of Operating System or the file system that works differently
on other OS-es.

* Filenames are case sensitive on some OS-es (e.g. Windows). They used to be restricted to 8.3. Make sure you are within the restriction of every OS you might want to use.
* Directory path: (slash or backslash or something else?) use the os.path methods.
* os.path.expanduser('~') works on both Linux and Windows, but the root of a Linux/Unix file system starts with a slash (/) and on Windows it is c:\ and d:\ etc.
* On Linux/Unix you have user 'root' and on Windows 'Administrator'
* File permissions are different on Linux and Windows.
* Stay away from OS specific calls, but as a last resort use os.name or sys.platform to figure out which os is this. os.name is 'posix' on Linux and 'nt' on Windows.
* For GUI use wxWindows that has a native look on Windows and Gnome look on Linux.
* Pay attention to any 32/64 bit issues. Big/Little Endian issues.
* Some modules might be OS specific. Check the documentation.
* Pay attention to the use of os.system and subsystem modules.


