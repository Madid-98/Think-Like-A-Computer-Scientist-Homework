# Write a program that asks the user for the number of sides,
# the length of the side, the color, and the fill color of a regular polygon.
# The program should draw the polygon and then fill it in.
#
#

import turtle

wn = turtle.Screen()
polygon = turtle.Turtle()


numberOfSides = int(input("Number of sides on the polygon: "))
lengthOfSides = int(input("Length of sides: "))
fillColour = input("Choose Line Colour: ")
lineColour = input("Choose Fill Colour: ")

angle =  360 / numberOfSides


polygon.begin_fill()
polygon.color(fillColour, lineColour)

for i in range(numberOfSides):
    polygon.forward(lengthOfSides)
    polygon.right(angle)

polygon.end_fill()

turtle.done()