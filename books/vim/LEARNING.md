First thing to know is how to exit (quit) from vim Press ESC then type :q


Vim is very different from othere editors.
Most editors have a single mode of operation in which you can edit text.
Navigation is limited and for many functions you need to use the menu system or the mouse.
Vim has several modes of operation, the important ones are called
* Normal mode (aka. navigation mode)
* Insert mode (aka. typing mode)
* Command mode
When we open a file by default we are in Normal mode.
Now you can navigate around with the arrows.
A lot more navigation options will come later.


The next thing to try is a basic edit cycle.
Press `i` to move from `Normal` to `Insert` mode. Then type some text and press `ESC` to
go back to `Normal` mode. You can repeat this several times.
I think one of the keys to use vim efficiently is to have short editing sessions
that are finished by pressing `ESC`. While in most cases you can use the arrow to move around
even when you are in `Insert` mode, I don't suggest to do that.
Now that you have edited the file you can's simply use `:q` to quit from vim as the file has changed.
Either you press `:q!` meaning quit without saving or press `:wq` meaning write out the file (save)
and then quit.


