###importing library
from turtle import *
import math

#settingupscreenstatus
setup(500,500)



# FUNCTIONS
def whileDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides += 1

def forDrawnShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    for s in range(sides):
        turtle.forward(50)
        turtle.right(angle)

def drawHouse(turtle,numSides,chosenColor):
    screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))




# RUNNING CODE

gorge = Turtle() #create turtle
gorge.turtlesize(2,2)#makes turtle longer
gorge.pensize(5)#makes pen larger
gorge.pendown()





#whileDrawShape(gorge,4,"green")
#gorge.penup()
#gorge.forward(100)
#gorge.pendown()
#forDrawnShape(gorge,5,"pink")
#whileDrawShape(diana.5,red)




#closes window on click
exitonclick()
