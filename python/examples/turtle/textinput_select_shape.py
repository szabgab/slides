import turtle

t = turtle.getturtle()

res = turtle.textinput("Shape?", "Which shape shall I draw? rectangle or triangle ?")
print(res)
if res == 'triangle':
    t.circle(100, steps=3)
elif res == 'rectangle':
    t.circle(100, steps=4)
else:
    pass
    

turtle.exitonclick()
