import turtle

t = turtle.getturtle()

res = turtle.numinput("Angles?", "How many angles?", default=3, minval=3, maxval = 180)
print(res)
t.circle(100, steps=int(res))

turtle.exitonclick()
