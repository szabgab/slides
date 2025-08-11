# SQLite exception handling (during INSERT)

* The internal exception handling should be enough, but apparently it is not
* See [this](https://github.com/crystal-lang/crystal-sqlite3/issues/52) report

{% embed include file="src/examples/sqlite/insert_exception.cr" %}


