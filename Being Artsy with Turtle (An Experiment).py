import turtle
import random

def rings(x_location, y_location, color): # defining function to draw olympic rings more efficiently
    """ (int, int, str) -> void
    Definition: Draws an olympic ring at given coordinates and color
    """
    olympic_rings = turtle.Turtle() # Olympics Logo drawn using multiple colors
    olympic_rings.penup() # ensures pen is up when moving from coordinate to coordinate
    olympic_rings.goto(x_location, y_location) # sends turtle to new location as specified by input argument
    olympic_rings.pencolor(color) # selects color of olympic ring
    olympic_rings.pendown()
    olympic_rings.circle(60) # specifies size of circle drawn

def my_triangle(length, color): # defining customizable function with 2 parameters: length and color
    """ (int, str) -> void
    Definition: Draws a customizable triangle of given length and color
    """
    triangle = turtle.Turtle() # Customizable Shape, drawn using a function with 2 parameters
    
    triangle.fillcolor(str(color)) # assigns type of color triangle will be filled with
    triangle.begin_fill()
    
    triangle.speed(random.randint(5, 10)) # integration of random number to edit speed at which drawing is drawn
    triangle.penup()
    triangle.goto(-200,-300) # assigning coordinates to start drawing the triangle at
    triangle.pendown()
    for i in range(3): # for loop used to draw the three sides of the triangle
        triangle.left(120) 
        triangle.forward(length)
    
    
    triangle.end_fill()


def my_drawing():
    """ () -> void (this function takes no input argument)
    Definition:
    Draws a customizable triangle of user inputted length and color, at a random speed
    Draws the first letter of my name using a for loop
    Draws a Magenta Cross with a Square centered in the middle
    Draws Olympic Games Logo, using given x, y coordinates and color 
    """
    
    length = int(input("Specify the length of the sides of the triangle: (100-500 works ideally): ")) # allows user to input choice of length for triangle 
    color = (input("Specify the color of the triangle: ")) # allows user to input choice of color for triangle
    
    
    # Drawing new shape: Custom Triangle
    custom_triangle(length, color) # calling custom triangle function using user-inputted arguments
    
    
    
    # Drawing new shape: Symmetrical Polygon (Magenta Cross with Square centered in Middle)
    polygon = turtle.Turtle() # Shape drawn using a for loop
    
    polygon.speed (0) # sets polygon drawing speed to fastest 
    polygon.penup()
    polygon.goto(-100, 350) # moves turtle to selected coordinate to begin drawing next shape
    polygon.pendown() 
    
    polygon.fillcolor("magenta") # sets multi-square symmetrical cross shape to a magenta color 
    polygon.begin_fill()
    
    for i in range(4): # for loop to draw the multi-square symmetrical cross shape
        polygon.forward(50)
        polygon.left(90)
        polygon.forward(50)
        polygon.right(90)
        polygon.forward(50)
        polygon.right(90)
        polygon.forward(50)
        polygon.left(90)
        polygon.forward(50)
        polygon.right(90)
    
    polygon.end_fill() # required to fill polygon with color
    
    
    # Drawing 5 new shapes: The Five Rings of the Olympics Logo 
    rings(0, 0, "black") # Calls rings function with appropriate x, y coordinates and color
    rings(-100, 0, "blue") # Calls rings function with appropriate x, y coordinates and color
    rings(-50, -50, "yellow") # Calls rings function with appropriate x, y coordinates and color
    rings(50, -50, "green") # Calls rings function with appropriate x, y coordinates and color
 










