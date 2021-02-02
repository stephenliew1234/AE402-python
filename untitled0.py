import turtle
alex=turtle.Turtle()
alex.shape("turtle")
alex.penuo()
for i in range(0,100,5):
    alex.forward(30+i)
    alex.left(30)
    alex.stamp()

