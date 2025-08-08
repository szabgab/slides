# Bash functions

Creating an alias for this might be difficult because of the parameter passing but we can create a function.


Add the following to ~/.bashrc and then type **source ~/.bashrc**


Then we can write **epm Module::Name**.


```bash
function epm(){
    vim $(perldoc -lm $*);
}
```




