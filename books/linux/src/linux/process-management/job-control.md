# Job control

* jobs
* fg
* bg
* Ctrl-C
* Ctrl-Z

"**jobs**" are processes related to the current shell.


* Run this **command**: **(while [ 1 ]; do (date; sleep 1); done)**
* suspend job: Ctrl-Z     SIGTSTP   (same as kill -20)  = stop for now
* **bg [job]** will move the specific (or current) job to the background.
* **fg [job]** will move the specific (or current) job to the foreground.

* **command &amp;** run in the background.

* **jobs** will show all the background jobs
* %number - reference to a job number
* %string - job whose name begins with string
* %?string - job whose name contains string
* %+ or %% - current job
* %- - previous job
* Ctrl-C     SIGINT    (same as kill -2)   = please die
* **kill [-signal] job** will send a signal to the given process.





