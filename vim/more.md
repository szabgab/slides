# More of Vim
{id: vim-more}

## Repeate commands
{id: repeate-commands}

{aside}

Many key combinations can be preceeded with a number that will indicate the number of repetitions we would like to have.
{/aside}

```
3dd            Delete 3 rows
4l             Move 4 characters to the right.  
5(left-arrow)  Move 5 characters to the left.
2dw            Delete 2 words.
```


## Repeat last change
{id: repeate-last-change}
{i: .}

* Make some change. (e.g. switch to insert mode, type in "hello world"; click ESC)
* Press **.**
* The text "hello world" will be inserted again.
* Press **3.**
* The text "hello world" will be inserted 3 more times.



## Search
{id: search}
{i: /}
{i: ?}
{i: n}
{i: N}
{i: *}
{i: #}

```
search forward:  /
search backward: ?
search again: n or N (in reverse)
search current word: *
search current word backwards: #


:set ignorecase
```


## Search and replace: substitute
{id: search-and-replace}
{i: /}
{i: s}

```
:%s/Old/New/              Replace Old by New.
:%s/^    /\t/             Replace leading 4-spaces by a tab.
:%s/$/./                  Put a . at the end of every line.
:'&lt;,'&gt;s/...         Subtitute in range.
```

To select range press **v** and then use the navigation keys. Then hit **:**



## Search and replace: substitute modifiers
{id: search-and-replace-modifiers}

```
:%s/Old/New/c             Ask for confirmation before every substitute.
:%s/Old/New/g             Multiple replaces on the same line.

:%s/Old/New/gc            Both.
```


## help
{id: vim-help}
{i: :help}

```
:help
:h
```

* It will split the window.
* You can jump between the help window and the other editor window by **Ctrl-w Up** and **Ctrl-w Down**.
* You can close the help part by typing **:q** while you are in the help window.



## Editing another file
{id: editing-another-file}

```
:e filename
```


## Switching buffers
{id: switching-buffers}
{i: :ls}
{i: :bn}
{i: :bp}
{i: :bN}
{i: :bd}
{i: :b TAB}


<a href="http://vimcasts.org/episodes/working-with-buffers/">Working with buffers</a>



```
:ls   list buffers

:bn     next buffer
:bp     previous buffer

:bN     switch to buffer N
:b TAB  cycle thorugh the names of the files in the buffers

:bd     delete current buffer
:bd3    delete buffer number 3
```


## Switching between last two buffers in vim
{id: switching-last-two-buffers}
{i: Ctrl-6}
{i: Ctrl-^}

```
:ls

a  - active buffer (the one we see in the window)
h  - hidden buffer (not in the window and has unsaved changes )
#  - alternate buffer
+  - buffer modified (unsaved)
```

```
To switch back-and-forth two buffers:

Ctrl-^ (Ctrl-Shift-6)
Ctrl-6
```


## Visual modes
{id: visual-mode}
{i: v}
{i: Shift-v}
{i: Ctrl-v}

```
v         - Visual mode from here to cursor.
Shift-v   - Visual mode this line till the line of the cursor.
Ctrl-v    - Vertical visual mode. Block or rectangular edit.

Use the arrow key and other navigation keys to move cursor.

Ctrl-V, select rectangular, x  - delete the selected characters.
```


## Indentation
{id: indentation}

```
Press &gt;&gt; to indent current line
Press N&gt;&gt; to indent N lines
Press &lt;&lt; to outdent current line
Press N&lt;&lt; to outdent N lines

Press == to autoindent currentline.
Press N== to autoindent N lines.
```


Select rows in Visual mode


```
Press &gt; to indent the selected lines.
Press N&gt; to indent N time.
Press &lt; to unindent

Press = to autoindent.
```

{aside}

As vim looses the visual selection we need a solution to allow us to indent more than once.
Press '.' to repeate the previous action to further indent or press 'u' to undo the extra indentation.
Alternatively one can map keys to keep the selection after indentation.
[Indentation commands](http://vimcasts.org/episodes/indentation-commands/)
{/aside}


## String completition in insert mode
{id: string-completition}
{i: Ctrl-N}
{i: Ctrl-P}

* Ctrl-N - by searching forward
* Ctrl-P - by searching backwards





## Shell commands
{id: shell-commands}
{i: :!ls}
{i: :!pwd}

```
:!ls
:!pwd
```


## Jump to character in current line
{id: jump-to-character}
{i: f}
{i: F}
{i: ;}
{i: ,}

```
f C    will jump to the first occurance of C to the right.
F C    will jump to the first occurance of C to the left

;  will repeat f or F
,  will reverse f or F
```

Any of those can be prefixed by number.



## Windows
{id: windows}
{i: m}
{i: '}

```
Ctrl-w s        horizontal split same file
Ctrl-w v        vertical split same file

:sp filename    horizontal split with other file
:vsp filename   vertical split with other file

Ctrl-w w        Cycle through the open windows
Ctrl-w arrow    Move between windows.  (also Ctrl-w [hjkl] work)

Ctrl-w +        Increase window
Ctrl-w -        Decrease window   (or use the mouse)
Ctrl-w =        Reset windows (equalize them)
Ctrl-w _        Maximize current window vertically
Ctrl-w |        Maximize current window horizontally

Ctrl-w r        Rotate windows
Ctrl-w R        Rotate windows in the other direction
Ctrl-w [HJKL]   Move windows

Ctrl-w c        Close window
:q              Close current window
:only           Close every window except the current one

:help ctrl-w
```


<a href="http://vimcasts.org/episodes/working-with-windows/">Working with windows</a>




## Mark
{id: mark}

```
ma          Will set mark a.
m{a-zA-Z}   Any letter can be used as a mark.

'a          Jump to mark a in current buffer.
```


## Registers
{id: registers}
{i: "ayy}
{i: "Ayy}
{i: "ap}

```
"ayy  will copy the current line into register 'a'

"Ayy  will append the current line to the register 'a'


"ap   will paste the content of register 'a'.

To list the content of all the registers, type :reg
```



## Change encoding
{id: change-encoding}
{i: set fileencoding}
{i: converted}
{i: utf8}


Sometimes you have files in encodings you don't want, sometime you'll see in the status line that the file is
<b>converted</b>. You can change the encoding of the file to utf8 by:



```
:set fileencoding=utf8
:w
```


## Current filename
{id: current-filename}

Copy (yank) the current file (buffer) name to clip-board so you can paste it using p. 


```
:let @" = expand("%")
```

Copy the full path:


```
:let @" = expand("%:p")
```



## Show rownumbers
{id: show-row-numbers}
{i: :set number}

```
:set number    - show line numbers
:set nonumber  - hide line numbers
:set number!   - toggle line numbers
```


## Show invisible characters
{id: show-invisible-characters}
{i: :set list}

* tab
* new-line
* [set list](http://vimcasts.org/episodes/show-invisibles/)


```
:set list
:set nolist
:set list!
```


## ~/.vimrc
{id: vimrc}
{i: .vimrc}
![](examples/vimrc)


## Embed vim settings in source code
{id: embed-vim-settings-in-source-code}
{i: vim:}


In a C file:



```
/*
  vim:sw=4:
*/
```

In a Perl file


```
# vim:expandtab
# vim:tabstop=4
```

In a JavaScript file


```
// vim:expandtab
// vim:tabstop=4
```

modline turns this feature on


modlines sets the number of lines to check

{i: set modline}
{i: set modlines}

```
:set modline
:set modlines=10
```


## TABs vs. Spaces
{id: tabs-vs-spaces}


<a href="http://vimcasts.org/episodes/tabs-and-spaces/">screencast</a>



* tabstop = 4
* softtabstop = 4
* shiftwidth = 4
* expandtab



## Videos
{id: videos}

* [Vimcasts - free screencasts about the text editor Vim](http://vimcasts.org/)
* [Vim for Perl development (video)](http://perltv.org/v/vim-for-perl-development)
* [More Instantly Better Vim](http://www.youtube.com/watch?v=aHm36-na4-4) OSCON 2013 talk by Damian Conway



## Vim Resources
{id: vim-resources}

* Run **vimtutor** on the Linux command line.
* Using the menus of **gvim** to find the command and then execute the key combination
* Use [vimium](https://github.com/philc/vimium) in Chrome or [vimperator](http://www.vimperator.org/) for Firefox to reuse the same key-bindings.
* [Vim Adventures](http://vim-adventures.com/)
* [vimgifs](http://vimgifs.com/)
* [Vim by Patrick Schanen](https://vim.zeef.com/patrick.schanen)
* [Vim Videos by Derek Wyatt](http://derekwyatt.org/vim/tutorials/)
* [usevim](http://usevim.com/)
* [Best of Vim Tips](http://zzapper.co.uk/vimtips.html)
* [Seven habits of effective text editing](http://www.moolenaar.net/habits.html) by Bram Moolenaar the developer of vim.
* [vimregex](http://vimregex.com/)
* [Learn Vimscript the Hard Way](http://learnvimscriptthehardway.stevelosh.com/)
* [VimAwesome](http://vimawesome.com/) Awesome Vim Plugins from accross the Universe.
* [vim](http://www.vim.org/)
* [vi/vim graphical cheat sheet](http://www.viemu.com/vi-vim-cheat-sheet.gif)





