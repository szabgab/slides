# Command history

* history
* HISTFILE
* !
* Ctrl-r

Commands executed in the shell are saved in a file. By default in **~/.bash_history**
but the filename is controllable by the **HISTFILE** environment variable.
HISTFILESIZE can be used to configure the number of lines saved in that file.
HISTSIZE can be used to control the number if lines save in the memory during a session (before saving it to the file)
The actual file is written when the shell exits. If there are multiple shells open, each will have its own history in memory
and each will write it to the file, the second exiting will overwrite the file written by the first one.
Use the **history** command to list the content of history buffer. Use ! N to run command N, or ! -N  or ! name.

* Up/Down arrows
* history
* !!    - the last comand
* ! N   - command number N
* Ctrl-r  -  reverse-i-search
* man bash   to see even more options.



