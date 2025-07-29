# cd in a function

* getcwd
* chdir


In this example we have a function in which we change to a directory and then when we are done we change back to the original directory.
For this to work first we save the current working directory using the `os.getcwd` call. Unfortunatelly in the middle of the code there
is a conditional call to `return`. If that condition is `True` we won't change back to the original directory. We could fix this by
calling `os.chdir(start_dir)` just before calling `return`. However this would still not solve the problem if there is an exception
in the function.


{% embed include file="src/examples/context/no_context_cd.py" %}

{% embed include file="src/examples/context/no_context_cd_tmp.out" %}

{% embed include file="src/examples/context/no_context_cd_opt.out" %}

* In the second example `return` was called and thus we stayed on the /opt directory.:w


