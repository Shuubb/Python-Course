import math
from turtle import *

class HouseProperties:
    HeightOfHouse = 250
    WidthOfHouse = HeightOfHouse

    HeightOfRoof = HeightOfHouse/2

    HeightOfDoor = HeightOfHouse/3
    WidthOfDoor = WidthOfHouse/5

    HeightOfWindows = WidthOfDoor*(3/4)
    WidthOfWindows = HeightOfWindows

def DrawRectangle(Width, Height, Fill):
    setheading(0)

    penup()
    forward(Width/2)
    pendown()

    if Fill == True:
        begin_fill()
    for x in range(2):
        left(90)
        forward(Height)
        left(90)
        forward(Width)
    if Fill == True:
        end_fill()

def DrawTriangle(Width, Height, Fill):
    setheading(0)

    penup()
    forward(Width/2)
    pendown()

    setheading(90)

    SidesOfRoofSz = math.sqrt((Width/2)**2 + Height**2)
    AnglesOfRoofSz = math.degrees(math.atan(Height/(Width/2)))

    if Fill == True:
        begin_fill()
    left(AnglesOfRoofSz)
    forward(SidesOfRoofSz)
    left(2*AnglesOfRoofSz)
    forward(SidesOfRoofSz)
    if Fill == True:
        end_fill()

def GoWithoutDraw(Width, Height):
    penup()
    goto(Width, Height)
    pendown()
    
#Drawing a house:

#Step 1: Drawing the square
#speed(30)
width(7)
color("purple")

HP = HouseProperties()

DrawRectangle(HP.WidthOfHouse, HP.HeightOfHouse, True)

#Step 2: Drawing the door
color("yellow")

GoWithoutDraw(0, 0)

DrawRectangle(HP.WidthOfDoor, HP.HeightOfDoor, True)

#Step 3: Drawing the roof
color("Green")

GoWithoutDraw(0, HP.HeightOfHouse)

DrawTriangle(HP.WidthOfHouse, HP.HeightOfRoof, True)

#Step 4: Drawing the Windows
color("brown")

GoWithoutDraw(-HP.WidthOfHouse/4, HP.HeightOfHouse*(3/4) - HP.HeightOfWindows/2)

DrawRectangle(HP.WidthOfWindows, HP.HeightOfWindows, True)

GoWithoutDraw(+HP.WidthOfHouse/4, HP.HeightOfHouse*(3/4) - HP.HeightOfWindows/2)

DrawRectangle(HP.WidthOfWindows, HP.HeightOfWindows, True)

exitonclick()