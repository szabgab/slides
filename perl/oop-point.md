# Object Oriented Perl
{id: object-oriented-perl5-point}


## Point
{id: perl5-oop-point}

![](examples/perloop/point/eg/point.pl)
![](examples/perloop/point/lib/Point.pm)


## Point3d: Subclassing Point
{id: perl5-oop-point-subclass}

![](examples/perloop/point/lib/Point/3D.pm)
![](examples/perloop/point/eg/point3d.pl)



## Exercise: Point::Small
{id: perl5-oop-exercise-point-small}


Create a class called Point::Small a subclass of Point
that will allow coordinates only between
0 and 100. Create a script point_small.pl that uses the new
Point::Small class and checks if it works and fails correctly.


## Solution: Point::Small
{id: perl5-oop-solution-point-small}

![](examples/perloop/point/lib/Point/Small.pm)


## Line - composition
{id: perl5-oop-line}

![](examples/perloop/point/eg/line.pl)
![](examples/perloop/point/lib/Line.pm)


## Line3D - composition and subclassing
{id: perl5-oop-line3d}

![](examples/perloop/point/eg/line3d.pl)
![](examples/perloop/point/lib/Line3D.pm)


## Indirect calling
{id: perl5-oop-indirect-calling}


The difference between



```
X->new
new X
```



