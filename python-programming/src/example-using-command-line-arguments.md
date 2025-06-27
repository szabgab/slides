# STDIN vs Command line arguments

If we run this script without any command-line parameters it will print out usage information.

If we give it two parameters it will treat the first one as the name of an input file and the second as the name of an output file.


* First try this; Then repeate. We must type in the same path again and again. Boring and error-prone.

{% embed include file="src/examples/basics/convert_stdin.py" %}

* We could use a Tk-based dialog:
* Still boring (though maybe less error-prone)

{% embed include file="src/examples/basics/convert_with_tk_dialog.py" %}

* The command line has
* History!

{% embed include file="src/examples/basics/convert_argv.py" %}


