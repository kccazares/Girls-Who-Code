from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:

mike = Turtle()
mike.pensize("3")
mike.pendown()

#####FUNCTION


def drawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides+=1
###########################
    #### RUNNING PROGRAM


another = True

while another == True:
        print("How many sides do you want?")
        numSides = int(input())
        
        print("What color do you want your shape to be?")
        chosenColor = input()
        
        drawShape(mike,numSides,chosenColor)
        print("Do you want another shape?")
        answer = input()
        if (answer == "no"):
            another = False

        

        




# Close window on click.
exitonclick()
