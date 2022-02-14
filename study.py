import turtle

def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        
        turtle.forward(50)
        turtle.right(60)

turtle.shape('turtle')
turtle.shapesize(5)
turtle.color('black', 'blue')
turtle.speed(10)

david()

turtle.backward(200)

david()

turtle.hideturtle()