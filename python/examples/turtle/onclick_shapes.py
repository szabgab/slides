import turtle
import time

s = turtle.getscreen()
t = turtle.getturtle()

#s.onclick(lambda x, y: t.left(10) )
s.onclick(lambda x, y: print(x, y) )

#s.mainloop()

while True:
    t.forward(1)
    #time.sleep(0.1)

