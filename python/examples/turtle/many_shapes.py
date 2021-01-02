import turtle

t = turtle.getturtle()

while True:
    res = turtle.numinput("Angles?", "How many angles?", default=3, minval=3, maxval = 180)
    if res is None:
        break
    t.clear()
    print(res)
    t.circle(100, steps=int(res))

