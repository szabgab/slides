import turtle

t = turtle.getturtle()

for i in range(4):
    t.forward(50)
    t.right(90)
t.goto(25, 25)
t.goto(50, 0)

input('Press ENTER to quit')
