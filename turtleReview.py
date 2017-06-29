
###importing library
from turtle import *
import math

#settingupscreenstatus
setup(500,500)



# FUNCTIONS
def whileDrawShape(turtle,chosenColor):
    turtle.pencolor(chosenColor)
    drawnSides = 0
    

    while drawnSides < 4:
        turtle.forward(50)
        turtle.right(90)
        drawnSides += 1

def forDrawnShape(turtle,chosenColor):
    turtle.pencolor(chosenColor)
    drawnSides = 0
    

    for s in range(3):
        turtle.forward(50)
        turtle.left(120)
        
def makeHouse(turtle,color):
    turtle.pendown
    turtle.pencolor(color)
    drawnsides = 4
    




# RUNNING CODE

house = Turtle() #create turtle
house.turtlesize(2,2)#makes turtle longer
house.pensize(5)#makes pen larger
house.pendown()

print("Hello, I'm Jake from state farm, your recently burned down... so sorry.")
print("As your insurance provider I will give you a new house!!!")

another = True


while another == True:
    #print("How many sides????")
    #numSides = int(input())

    print("What color do you want your house to be?")
    chosenColor = input()

    whileDrawShape(house,chosenColor)
    forDrawnShape(house,chosenColor)
    
    print("Do you want another house?")
    answer = input()

    if (answer == "No" or answer == "no thanks"):
        another = False
    elif (answer == "yes" or answer == "yeah sure"):
        house.penup()
        house.forward(90)
        house.pendown()
        another = True



#whileDrawShape(gorge,4,"green")
#gorge.penup()
#gorge.forward(100)
#gorge.pendown()
#forDrawnShape(gorge,5,"pink")
#whileDrawShape(diana.5,red)




#closes window on click
exitonclick()
