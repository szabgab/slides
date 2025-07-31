# Exercise: fork return data

Create a script that will go over a list of numbers and does some computation on each number.

{% embed include file="src/examples/fork/compute.py" %}

Allow the child process to return data to the parent process. Before exiting from the child process, serialize the data-structure you want to send back and save
in a file that corresponds to the parent process and the child process. (eg. created from the PID of the paraent process and the PID of the child process)
In the parent process, when one of the children exits, check if there is a file corresponding to this child process, read the file and de-serialize it.



