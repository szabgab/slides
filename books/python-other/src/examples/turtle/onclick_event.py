import turtle
import time

scr = turtle.getscreen()
t = turtle.getturtle()

#s.onclick(lambda x, y: t.left(10) )
scr.onclick(lambda x, y: print(x, y), btn=1 )
scr.onclick(lambda x, y: print('middle'), btn=2 )
scr.onclick(lambda x, y: print('right'), btn=3 )

scr.mainloop()

#while True:
#    t.forward(1)
#    #time.sleep(0.1)

