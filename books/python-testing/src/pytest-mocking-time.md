# Pytest: Mocking time

There are several different problems with time

* A login that should expire after 24 hours. We don't want to wait 24 hours.
* Some code that must be executed on certain dates. (e.g. January 1st every year)


