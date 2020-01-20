# Introduction to Vim
{id: vim}

## Install vim
{id: install-vim}

* Linux vi is mapped to vim, but it might not have all the features.
* Ubuntu: sudo apt-get install vim
* Red Hat: sudo yum install vim
* Windows: [from vim](http://www.vim.org/)



## First editing session - create file
{id: create-file}

1. Type **vim hello.txt**
1. Press **i** to switch to insert mode.
1. Type in "hello world".
1. Press **ESC** to switch back to command mode.
1. Type  **:wq** this will write out the file and quit vim.



## Change file
{id: change-file}

1. Type **vim hello.txt**. The editor opens, the cursor is on the "h" of the "hello".
1. Press **~** to change the case of "h" to be "H"
1. Press **5l** (lower case L) to move 5 characters to the "w".
1. Press **rW** to replace "w" by "W".
1. Press **o** to switch to insert mode on the line below.
1. Type in: "and welcome to vim!"
1. Press **ENTER** and continue typing: "This is the 3rd line.
1. Press **ESC** to switch back to command mode.
1. Type  **:wq** this will save the file and quit vim.



## Visual Insert
{id: visual-insert}

1. Type **vim hello.txt**. The editor opens, the cursor is on the "H" of the "Hello".
1. Press **2yy** followed by **p**. The first 2 lines were yanked into memory (copied) and the pasted above the current line.
1. Press **Ctrl-v** to switch to visual mode.
1. Press **2j** to mark 2 more lines under the current line.
1. Press **I** (Shift i) to switch to insert mode.
1. Type in "vim! "
1. Press **ESC**
1. After a second "vim! "  will appear on the second and third lines as well.
1. Type **:wq** to write file and quit vim.



## Visual Append
{id: visual-append}

1. Type **vim hello.txt**.
1. Press **$** (Shift-4) that will jump to the end of the current line.
1. Press **Ctrl-v** to switch to visual mode.
1. Press **j** 3 time to mark 3 additional rows.
1. Press **A** (Shift a) to switch to insert mode appending to the end of the row.
1. Type in " end"
1. Press **ESC**
1. After a secon " end" will appear at the end of 3 other lines.
1. Type **:wq** to write and quit.



## Modes of vim
{id: modes-of-vim}

* Normal Mode (aka. Command Mode or Navigation mode)
* Insert Mode
* Command line
* Visual Mode



## ESC
{id: esc}
{i: ESC}

{aside}

Before learning anything else, it is worth remembering that pressing ESC several times will always
bring you back to **Normal mode**.
{/aside}


ESC - get out of trouble and back to Command mode




## Save (write) file
{id: save-file}
{i: :w}

```
:w                Write under current filename.
:w filename       Save-as.
```



## Quit
{id: quit-vim}
{i: :q}
{i: :q!}
{i: :wq}


These are the ways to quit vim. (when in <b>Normal mode</b> press either of the following:)



```
:q    quit            - If there was no change since last write.
:q!   force-quite     - Abandon changes.
:wq   write-and-quit
```


## Basic moves
{id: basic-moves}
{i: h}
{i: j}
{i: k}
{i: l}
{i: 0}
{i: ^}
{i: $}
{i: :20}
{i: :goto 40}

{aside}
Remember, you can use these in Normal mode only.
{/aside}


```
Move around h (left) j (down) k (up) l (right) or the 4 arrows
0         - jump to beginning of the line
^         - jump to first non white-space of the line
$         - jump to end of line
:20       - go to line number 20
:goto 40  - go to character 40
```


## Switch to insert/edit mode
{id: switch-to-insert-mode}
{i: i}
{i: I}
{i: a}
{i: A}
{i: o}
{i: O}

```
i     - (insert)  right before (to the left of) the current character.
I     - (Insert)  right before first non-blank in the current line.
a     - (appaned) right after the current character.
A     - (Apppend) right after end of line.
o     - add new empty row below.
O     - add new empty row above.
```

{aside}
Remember, ESC will take you from insert mode back to normal mode.
{/aside}



## Delete row/word/character
{id: delete}
{i: dd}
{i: dw}
{i: x}

```
dd   delete current row
dw   delete word
x    delete current character
```


## Undo - Redo
{id: undo-redo}
{i: u - undo}
{i: :redo}

```
u      - undo
:redo  - redo
```


## Copy/Paste (Yank/Paste)
{id: copy-paste}
{i: yy}
{i: p}
{i: P}

```
Yank: yy
Yank 4 rows:   4yy

Paste: p
Paste: P
```


## Switch characters
{id: switch-characters}
{i: xp}

```
xp  - switch current and next character.
```


## Exercise: vim intro
{id: exercise-vim-intro}

* Take the examples in the first few slides and type them yourself.



## Exercise: vim editing
{id: exercise-vim-editing}

* Create a text file and write a short-story.
* Involve deleting characters, words, and lines.
* Swicth between Insert mode and Normal command mode.
* Save the file, quit, open it again.



