# Absolute path



If we would like to load a module that is not installed in one of the standard locations, but we know where it is located on our disk,
we can set the "sys.path" to the absolute path to this directory. This works on the specific computer, but if you'd like to distribute
the script to other computers you'll have to make sure the module to be loaded is installed in the same location or you'll
have to update the script to point to the location of the module in each computer. This is not an ideal solution.


{% embed include file="src/examples/modules/load_from_absolute_path.py" %}



