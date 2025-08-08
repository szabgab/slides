# Stopped process demonstration

* In one window run **htop** and filter to 'perl'.
* In the second window run  **perl -e '&lt;STDIN&gt;'**
* Look at the htop display to see the process appearing with a state S
* Press **Ctrl-z** in the window with the process.
* Look at the htop display to see the process appearing with a state T
* **bg** will move the process to the background but the state will stay in T.
* **fg** will move it to the foreground and the state will change to S.
* **ENTER** will finish the process.
* Do the same with this example: **perl -e 'sleep 1 while 1'**
* In this case moving to the background will already move the process to S state.



