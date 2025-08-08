# tmux multiple session

```
$tmux                    - create new session (name 0)
$ echo "session 0"
$ Ctrl-b d               - detach

$ tmux                   - create new session (name 1)
$ echo "session 1"
$ Ctrl-b d               - detach

$ tmux new -s sample     - new session (name sample)
$ echo sample
$ Ctrl-b d               - detach

$ tmux ls
0: 1 windows (created Wed Jul 20 11:51:58 2016) [101x50]
1: 1 windows (created Wed Jul 20 11:52:02 2016) [101x50]
sample: 1 windows (created Wed Jul 20 11:54:53 2016) [101x50]

$ tmux a -t 1            - attach to session 1
$ Ctrl-b d
$ tmux a -t sample       - attach to session sample

$ Ctrl-b s               - list sessions and select another one
$ Ctrl-b $               - rename current session

$ tmux kill-session -t session-name     - or just exit the window with Ctrl-d
```



