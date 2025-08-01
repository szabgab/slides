import turtle

def house():
    trt = turtle.getturtle()

    for i in range(4):
        trt.forward(50)
        trt.right(90)
    trt.goto(25, 25)
    trt.goto(50, 0)

house()

turtle.exitonclick()
