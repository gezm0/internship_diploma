import turtle

turtle.shape('turtle')
turtle.shapesize(5)
turtle.color('red')
turtle.speed(1)

for step in range(6):
    turtle.forward(50)
    turtle.right(60)

turtle.hideturtle()