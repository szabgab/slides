# Keep remote session using screen

* screen

```
$ ssh remote
$ screen
  ... do stuff ...
  get disconnected

$ ssh remote
$ screen -dr
  ... back where you were ...
```


* screen         - to start a new session.
* screen -dr     - to attach to an existing session.
* Ctrl-a Ctrl-d  - to detach from an existing session.



* Ctrl-a Ctrl-c    Create new Window
* Ctrl-a w         List Windows
* Ctrl-a 0         Jump to Window 0
* Ctrl-a ?         Help
* Ctrl-d           Close current window (close screen)




