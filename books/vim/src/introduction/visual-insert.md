# Visual Insert


1. Type **vim hello.txt**. The editor opens, the cursor is on the "H" of the "Hello".
1. Press **2yy** followed by **p**. The first 2 lines were yanked into memory (copied) and the pasted above the current line.
1. Press **Ctrl-v** to switch to visual mode.
1. Press **2j** to mark 2 more lines under the current line.
1. Press **I** (Shift i) to switch to insert mode.
1. Type in "vim! "
1. Press **ESC**
1. After a second "vim! "  will appear on the second and third lines as well.
1. Type **:wq** to write file and quit vim.




