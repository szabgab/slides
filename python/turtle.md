# Turtle
{id: turtle}


## Line
{id: turtle-line}
{i: getturtle}
{i: forward}
{i: exitonclick}

{aside}
Without the call to `turtle.exitonclick()` at the end of the program it would automatically close the window and we would not be able to see anything. This command installs an event-handler so when we click on the mouse it will end the application.
{/aside}

![](examples/turtle/line.py)



## Square (forward, left)
{id: turtle-square}
{i: forward}
{i: left}

![](examples/turtle/square.py)

## Circle
{id: turtle-circle}
{i: circle}

![](examples/turtle/circle.py)

## Square using the circle command
{id: turtle-square-by-circle}
{i: steps}

![](examples/turtle/square_by_circle.py)

![](examples/turtle/square_by_circle_set_angle.py)

## Triangle
{id: turtle-triangle}

![](examples/turtle/triangle.py)

## Move turtle without drawing (penup, pendown, goto)
{id: turtle-goto}
{i: penup}
{i: pendown}
{i: goto}

{aside}
Coordinates (0, 0) are in the middle of the screen.
{/aside}

![](examples/turtle/two_circles.py)


## Turtle house
{id: turtle-house}
{i: right}
{i: forward}
{i: goto}

![](examples/turtle/house.py)

## Turtle screen
{id: turtle-screen}
{i: getscreen}
{i: bgcolor}

![](examples/turtle/blue_screen.py)

## Tutle onclick - mouse click event
{id: tutrle-onclick}

![](examples/turtle/onclick_event.py)


## Turle Commands
{id: turle-commands}

* [docs](https://docs.python.org/library/turtle.html)


* forward(distance), fd
* backward(distance), bk
* left(angle),  lt
* right(angle),  rt
* goto(x, y)
* home()      goto(0,0)   - the center
* pos()      - get current position
* penup()
* pendown()
* clear()
* circle(radius), circle(radius, extent, steps)
* dot() ???

## Turtle Colors
{id: turtle-colors}

* Named Colors  [See the names](https://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm)
* Hex Code - use a color picker
* Color Tuple r,g,b each one goes from 0-1
* color
* pencolor
* fillcolor
* s.bgcolor
* begin_fill + end_fill

![](examples/turtle/change_turtle_color.py)
![](examples/turtle/fill_shape_by_color.py)

## Turtle shape
{id: turle-shape}

* shapesize
* shape('square')

![](examples/turtle/change_turtle_shape.py)

## Turtle speed
{id: turtle-speed}

* speed (1-10)

* pen(pencolor=, fillcolor=, pensize=, speed=)

## Undo the turtle
{id: turtle-undo}

* undo()
* undobufferentries()
* setundobuffer(17)

* clear()
* reset()
* showturtle()
* hideturtle()
* stamp()
* clearstamp(N)


## Create new turtle
{id: turtle-create-new}

x = turtle.Turtle()

## Clone a turtle
{id: turtle-clone}

y = t.clone()

![](examples/turtle/star.py)


![](examples/turtle/many_shapes.py)

![](examples/turtle/numinput_select_shape.py)


![](examples/turtle/textinput_select_shape.py)

![](examples/turtle/draw.py)

