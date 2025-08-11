# require

require - imports are global. This makes it hard to see in a file where some objects might come from
as they might have been required by some other file.

Similarly requiring a bunch of files in a directory is easy to do, but might make it a bit harder for
someone without an IDE to find the source of each object.

```
require "./directory/file"  # relative path to the cr file
require "./directory/*"     # all the cr files in the directory
require "./directory/**"    # all the cr files in the directory - recursively
require "some_name"         # Find it somewhere (standard library, src directory)
```

* You can put the `require` statements anywhere but you might want to be consistent in your project.
* Make sure you don't have circular requires.


