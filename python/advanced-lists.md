# Advanced lists
{id: advanced-lists}


## Change list while looping: endless list
{id: endless-list}
![](examples/advanced/endless_for.py)


Creating a Fibonacci series in a crazy way.




## Change list while looping
{id: change-list-while-looping}


Probably not a good idea...


![](examples/advanced/change_list_on_the_fly.py)
![](examples/advanced/change_list_on_the_fly.out)

Note, the loop only iterated 3 times, and it skipped value 3



## Copy list before iteration
{id: copy-list-before-iteration}

It is better to copy the list using list slices before the iteration starts.

![](examples/advanced/change_list_on_the_fly_copied.py)
![](examples/advanced/change_list_on_the_fly_copied.out)


## for with flag
{id: for-with-flag}
![](examples/advanced/for_with_flag.py)


## for else
{id: for-else}

The else statement of the for loop is executed when the iteration ends normally. (without calling break)

![](examples/advanced/for_else.py)


## enumerate
{id: enumerate}
{i: enumerate}
![](examples/advanced/enumerate.py)
![](examples/advanced/enumerate.out)


## do while
{id: do-while}
{i: do while}

There is no do-while in Python, but you can emulate it:

![](examples/advanced/do_while_pseudo.py)
![](examples/advanced/do_while.py)


## list slice is copy
{id: list-slice-copy}
![](examples/advanced/list_slice_is_copy.py)




