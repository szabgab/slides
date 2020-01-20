# X-Windows
{id: x-windows}

## X11
{id: x11}
{i: X11}
{i: xcalc}


X11 X-Windows is the mostly used windowing system for unix.
There are several window managers running on X11 which makes the capturing part difficult.
On unix machines we have a nice graphical calculator called xcalc.




## X11 Tools
{id: x11-tools}

* [X11::GUITest](https://metacpan.org/pod/X11::GUITest)
* [X11::Protocol](https://metacpan.org/pod/X11::Protocol)
* [LDTP](http://ldtp.freedesktop.org/) - Linux Desktop Testing Project



## X11::GUITest
{id: x11-guitest}
{i: X11::GUITest}

* Available since 2003 by Dennis K. Paulsen.
* [X11::GUITest](https://metacpan.org/pod/X11::GUITest)



## LDTP - Linux Desktop Testing Project
{id: ldtp}
{i: LDTP}

* [LDTP](http://ldtp.freedesktop.org/) Cross Platform GUI Test Automation tool
* [ldtp for Perl](https://github.com/ldtp/ldtp) by [SawyerX](http://blogs.perl.org/users/sawyer_x/2012/09/perl-on-ldtp-is-gaining-traction.html)



## Manual steps
{id: x11-manual-steps}

```
Launch the application manually and look at its title

xcalc
```


## X11: Launch the application
{id: x11-launch-application}
{i: StartApp}
{i: WaitWindowViewable}
{i: GetInputFocus}
![](examples/X/xcalc01.pl)


<command>perl examples/X/xcalc01.pl</command>
As you can see we only open the xcalc window and do not close it yet.
So now if you run this for a second time (without manually closing the first xcalc window)
you will see the error message and you'll see that the Main windows id is the same as previously
as the first windows was found first but the Focus is on another window, the one we have just
opened.




## Let's see the coordinates
{id: x11-coordinates}
{i: GetWindowPos}

```
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";
```
![](examples/X/xcalc02.pl)


<command>perl examples/X/xcalc02.pl</command>
Nice, but where exactly are these coordinates ?
Let's put the mouse to the top left corner.




## Where is this top left corner ?
{id: x11-top-left-corner}
{i: MoveMouseAbs}

```
MoveMouseAbs($x, $y);
```
![](examples/X/xcalc03.pl)

```
perl examples/X/xcalc03.pl
```


## And let's see the rest of the coordinates
{id: x11-coordinates-more}

```
MoveMouseAbs($x, $y);
sleep(2);
MoveMouseAbs($x+$width, $y);
sleep(2);
MoveMouseAbs($x+$width, $y+$height);
sleep(2);
MoveMouseAbs($x, $y+$height);
```
![](examples/X/xcalc04.pl)


<command>perl examples/X/xcalc04.pl</command>
The sleep() commands were added only so that we can see the mouse moving around.




## Smooth on the edges
{id: x11-smooth-edges}

```
MoveMouseAbs($x, $y);
foreach my $w (0..$width) {
   MoveMouseAbs($x+$w, $y);
}
foreach my $h (0..$height) {
   MoveMouseAbs($x+$width, $y+$h);
}
foreach my $w (0..$width) {
   MoveMouseAbs($x+$width-$w, $y+$height);
}
foreach my $h (0..$height) {
   MoveMouseAbs($x, $y+$height-$h);
}
```


<command>perl examples/X/xcalc05.pl</command>


![](examples/X/xcalc05.pl)


## Closing the window
{id: x11-closing-window}
{i: ClickMouseButton}
{i: SendKeys}

```
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";

MoveMouseAbs($x+2, $y-2);
ClickMouseButton M_LEFT;
SendKeys('c');
```


We could close the window by typing Alt-F4 but it does not work on my notebook as I
have set Alt-F4 to be something else.




So we can either click on the X in the top-right corner, or click on the X in the top
left corner, and then press C. We chose the latter.




The above code will probably work on most of the possible screen resolutions but
generally moving a fixed number of pixels might not be the best solution.



**perl examples/X/xcalc06.pl**

![](examples/X/xcalc06.pl)


## Placing the cursor on one of the buttons and clicking on it
{id: x11-moving-the-mouse}

```
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";

my $button_width = $width/5;
my $button_height = $height*0.8/8;
MoveMouseAbs($x + 2.5 * $button_width, $y+$height * 0.2 + 5.5 * $button_height);

ClickMouseButton M_LEFT;
```


Observing the xcalc application we see that it has 5 buttons in a row and 8 in a column.
At the top of the application there is another window which is about 20% of the total height, full width.




So first we calculate the size of a button and then the center of button "5".



perl examples/X/xcalc07.pl

![](examples/X/xcalc07.pl)


## So let's do all the calculations
{id: x11-calculations}

```
my ($x, $y, $width, $height) = GetWindowPos($Main);
print "$x $y $width $height\n";

my $button_width = $width/5;
my $button_height = $height*0.8/8;

MoveMouseAbs($x + 2.5 * $button_width, $y+$height * 0.2 + 5.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);

MoveMouseAbs($x + 4.5 * $button_width, $y+$height * 0.2 + 4.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);

MoveMouseAbs($x + 1.5 * $button_width, $y+$height * 0.2 + 4.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);

MoveMouseAbs($x + 4.5 * $button_width, $y+$height * 0.2 + 7.5 * $button_height);
ClickMouseButton M_LEFT;
sleep(2);
```


<command>perl examples/X/xcalc08.pl</command>

That would be 5 * 7 =


![](examples/X/xcalc08.pl)


## Fetch the list of Child Windows
{id: x11-child-windows}
{i: GetChildWindows}
{i: GetWindowName}

```
my @children = GetChildWindows $Main;

foreach my $id (@children) {
  my $name = GetWindowName($id) || '';
  print "Child: '$id'  '$name'\n";
}
```


<command>perl examples/X/xcalc11.pl</command>
Non of them has a title, this seem to be like a dead-end, but wait a second,
maybe we can find the location of the child windows.


![](examples/X/xcalc11.pl)


## Locate the Child Windows
{id: x11-locate-child-windows}

```
printf "Main      %6s %6s %6s %6s\n", GetWindowPos($Main);

my @children = GetChildWindows $Main;

foreach my $id (@children) {
  printf "%6s  %6s %6s %6s %6s\n", $id, GetWindowPos($id);
}
```

```
perl examples/X/xcalc12.pl


Main: 18874425
Focus: 18874425
Main           6     26    226    304
18874426       6     26    226    304
18874428     186    298     40     26
18874429     142    298     40     26
18874430      98    298     40     26
18874431      54    298     40     26
18874432      10    298     40     26
18874433     186    268     40     26
18874434     142    268     40     26
18874435      98    268     40     26
18874436      54    268     40     26
18874437      10    268     40     26
18874438     186    238     40     26
18874439     142    238     40     26
18874440      98    238     40     26
18874441      54    238     40     26
18874442      10    238     40     26
18874443     186    208     40     26
18874444     142    208     40     26
18874445      98    208     40     26
18874446      54    208     40     26
18874447      10    208     40     26
18874448     186    178     40     26
18874449     142    178     40     26
18874450      98    178     40     26
18874451      54    178     40     26
18874452      10    178     40     26
18874453     186    148     40     26
18874454     142    148     40     26
18874455      98    148     40     26
18874456      54    148     40     26
18874457      10    148     40     26
18874458     186    118     40     26
18874459     142    118     40     26
18874460      98    118     40     26
18874461      54    118     40     26
18874462      10    118     40     26
18874463     186     88     40     26
18874464     142     88     40     26
18874465      98     88     40     26
18874466      54     88     40     26
18874467      10     88     40     26
18874468      10     28    216     46
18874469      17     31    204     38
18874470     145     53     18     15
18874471     109     53     34     15
18874472      79     53     26     15
18874473      49     53     26     15
18874474      22     55     26     15
18874475      36     34    186     17
18874476      22     34     10     15
```
![](examples/X/xcalc12.pl)


## Using the keyboard
{id: x11-using-the-keyboard}

```
SendKeys("7*5=");
sleep(5);
```

```
perl examples/X/xcalc21.pl
```
![](examples/X/xcalc21.pl)


## Separate the keystrokes
{id: x11-separate-keystrokes}

```
SendKeys("7");
sleep(2);
SendKeys("*");
sleep(2);
SendKeys("5");
sleep(2);
SendKeys("=");
sleep(2);
```

```
perl examples/X/xcalc22.pl
```
![](examples/X/xcalc22.pl)



## Full solution for xcalc
{id: x11-xcals}

```
perl examples/X/xcalc.pl keyboard
perl examples/X/xcalc.pl mouse
```
![](examples/X/xcalc.pl)






