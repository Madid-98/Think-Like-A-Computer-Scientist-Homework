import turtle

#Functions

def startup():
    youngTurtle.hideturtle()
    youngTurtle.penup()
    ##youngTurtle.right(angle) we just want to go forward
    youngTurtle.forward(50)
    youngTurtle.pendown()
    youngTurtle.forward(20)
    youngTurtle.penup()
    youngTurtle.forward(20)
    youngTurtle.stamp()
    youngTurtle.penup()

    # go back to the middle and turn back around
    youngTurtle.right(180)
    youngTurtle.forward(90)
    youngTurtle.right(180)


wn = turtle.Screen()

youngTurtle = turtle.Turtle()
youngTurtle.shape("turtle")

youngTurtle.stamp()

n = 12
angle = 360 / n

startup()

for i in range(n):
    # draw the leg
    youngTurtle.hideturtle()
    youngTurtle.penup()
    youngTurtle.right(angle)
    youngTurtle.forward(50)
    youngTurtle.pendown()
    youngTurtle.forward(20)
    youngTurtle.penup()
    youngTurtle.forward(20)
    youngTurtle.stamp()
    youngTurtle.penup()

    # go back to the middle and turn back around
    youngTurtle.right(180)
    youngTurtle.forward(90)
    youngTurtle.right(180)

youngTurtle.shape("circle")

wn.exitonclick()

