# More UNIX commands implemented in modules

* pwd
* cwd
* basename
* dirname
* cp
* copy
* mv
* move

| Module | Usage | Comment |
| Cwd | $dir = cwd; | current working directory |
| File::Copy | copy "oldfile", "newfile"; |  |
|  | move "oldfile", "newfile"; | this works between file systems as well |
| File::Basename | basename "/a/b/c/file.pl"; | file.pl |
|  | dirname "/a/b/c/file.pl"; | /a/b/c |
| File::Path | mkpath("a/b/c") | (like mkdir -p) |
|  | rmtree("/") |  |
| File::Find |  |  |
| File::Find::Rule |  |  |


