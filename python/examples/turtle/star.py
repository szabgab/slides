import turtle

# based on the example in the documentation

t = turtle.getturtle()
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(100)
    t.left(190)
    if abs(t.pos()) < 1:
        break
t.end_fill()

turtle.exitonclick()
