# Exercise: Log::Dispatch


Take the examples/advanced-perl/log_dispatch.pl
and change it so only warnings are printed to the screen.
debug messages are printed to a log file.
The name of the file should be in the format YYYY-MM-DD.log
The log line should include the name file name and the line number where it was called.

Check out the strftime of the POSIX module and see how Log::Dispatch
allows you to provide a callback function.



