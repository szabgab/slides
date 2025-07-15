# X11: Launch the application

* StartApp
* WaitWindowViewable
* GetInputFocus

{% embed include file="src/examples/X/xcalc01.pl" %}


`perl examples/X/xcalc01.pl`

As you can see we only open the xcalc window and do not close it yet.
So now if you run this for a second time (without manually closing the first xcalc window)
you will see the error message and you'll see that the Main windows id is the same as previously
as the first windows was found first but the Focus is on another window, the one we have just
opened.


