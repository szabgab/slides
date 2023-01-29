import turtle

def screen_details():
    scr = turtle.getscreen()
    print(dir(scr))
    print(scr.screensize())
    print(scr.window_width())
    print(scr.window_height())

def draw_top_box():
    trt = turtle.getturtle()
    scr = turtle.getscreen()
    speed = trt.speed()
    print(speed)
    trt.speed(0)
    trt.penup()
    trt.setpos(20-scr.window_width()/2, scr.window_height()/2-20)
    trt.pendown()
    trt.setheading(0)
    trt.forward(scr.window_width()-40)
    trt.setheading(270)
    trt.forward(200)
    trt.setheading(180)
    trt.forward(scr.window_width()-40)
    trt.write("GitHub", font=("Arial", 30, 'normal'))
    trt.setheading(90)
    trt.forward(200)

    trt.speed(speed)

#turtle.bye()
def click(x, y):
    print('click at', x, y)
def button():
    print("button")

def main():
    trt = turtle.getturtle()
    scr = turtle.getscreen()
    scr.onclick(click)
    #scr.onkey(button,  'a')
    #scr.listen() # is needed to make the onkey settings work
    screen_details()
    draw_top_box()
    turtle.mainloop()

    #turtle.exitonclick()

main()
