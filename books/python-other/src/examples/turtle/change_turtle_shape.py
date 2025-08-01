import turtle

trt = turtle.getturtle()
trt.shapesize(3, 5)  # height, width , default is 1,1
trt.forward(50)


trt.shape('classic')
trt.shape('arrow')
trt.shape('circle')
trt.shape('triangle')
trt.shape('square')
trt.shape('turtle')

turtle.exitonclick()
