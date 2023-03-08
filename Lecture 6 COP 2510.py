#effect of break on nested structure 

##i = 7
##while i < 15:
   ## if i == 7:
     ##   break # the output will be 7 only because the break statement will break the loop and not print the rest of the numbers
    ##print(i)
    ##i += 2
    
    
    
#walrus operator and while loops #if we take parenthesis out  from line 15 we will see the "number is false" printed out because with the one 
# parenthisis out the number inputed is first compared to being negative or positive and then assigned to NUmber .
# # WHich is why the whole operation after that is not considered  
#The third parenthisis allows us to store integer in the varaible NUmber and then compare it 

#while(Number := int(input("Enter a positive number : "))) < 0:
 #   number = int(input("invalid. Enter a new number that is positive :"))
#print(f"Your number is {Number} ") 

#another method using continue
#while(Number := int(input("Enter a positive number : "))) < 0:
 #   continue 
#print(f"Your number is {Number} ")   


# another method 
#while(Number := int(input("Enter a positive number : "))) < 0:
    #print("invalid", end = '')
#print(f"Your number is {Number} ") 

# contniue from lecture 5 cop 2510
#enumerate is a standard function that allows us to 
# #m starts at 0 by default which means first item in list named m   
# 11th item in a list is not considered  hence 1 to 10 is considered in reality by the function
#for m ,n in enumerate(range(1,11)):
    #print(f"{m}*{n} = {m*n}")  
   
#for m ,n in enumerate(range(21,31)):
    #print(f"{m}*{n} = {m*n}") 
    
# we have the ability to set the value of m the start means m starts at 1  
#for m ,n in enumerate(range(21,31),start = 1):
    #print(f"{m}*{n} = {m*n}")  
    
    
#Turtle module
import turtle # this is a module that allows us to draw shapes and patterns 
from turtle import *  # the * is a while card character , 
# u will get a dialog box
name = turtle.textinput('Dialog Box', 'Enter name : ')# this is a dialog box that allows us to enter a name
print(name)

radius = turtle.numinput('Radius Box ', 'ENter radius :', default = 25, minval = 10, maxval = 300)# this is a dialog box that allows us to enter a radius

turtle.circle(radius)# this is a function that draws a circle with the radius inputed in the dialog box
turtle.clearscreen() # this is a function that clears the screen



# change shape or speed 
turtle.shape ("turtle")  #change cursor shape to turtle 
turtle.speed(0)#range is 0  to 10 ; means no animation

#drew a square 
for i in range (4) :
    turtle.fd(150)# you can use forward or # fd , backward or bk as movements
    turtle.dot(10, 'green') #through thus we get a green coloured dot on all corners   #10 indicates the radius of the dot and colour indicates the colour of the dot
    turtle.rt(90)#rt for right
     
turtle.clearscreen()  #clears the screen completely 
# draw a series of circles 
x, y = 300, 0 
turtle.penup() #enables the tutle to move without drawing 

turtle.setpos(x,y) #the turtle shape is a line with a cursor at the start 

for z in range (7) : # Through this entire fucntion we create 7 circles glued together in series 
    turtle.pendown() #opposite of penup
    turtle.circle(40)
    x+= 80
    turtle.penup() # THIS IS IMPORTANT BECAUSE IF WE DONT PUT THIS THE TURTLE WILL DRAW A LINE FROM THE END OF THE CIRCLE TO THE START OF THE NEXT CIRCLE
    turtle.setpos(x , y) # AFTER THE CIRCLE IS DRAWN THE TURTLE WILL MOVE TO THE NEXT POSITION TO DRAW THE NEXT CIRCLE
    
#draw pattern

NUM_CIR = 36 
ANGLE = 10
SPEED = 20

shape = turtle.textinput('Shape ', ' Enter shape') # or we can use turtle.shape('turtle')
turtle.shape(shape) # or we can use turtle.shape('turtle')
turtle.speed(SPEED) #
r = turtle.numinput('Radius ', 'ENter radius',default = 25, minval = 10, maxval = 300) #numinput is a function that allows us to input a number

for c in range (NUM_CIR): # this is a for loop that draws a series of circles,
    turtle.circle(r) # this is a function that draws a circle with the radius inputed in the dialog box
    turtle.left(ANGLE) # this is a function that turns the turtle to the left by the angle inputed in the dialog box
    
    
#This code is using the Turtle module in Python to create shapes and animations.

#The first line "import turtle" imports the turtle module, while the second line "from turtle import " imports all functions from the turtle module, represented by the wild card character ().

#The next few lines create a dialog box where the user can input their name, and it is stored in the variable "name".

#Another dialog box appears asking the user to enter a radius value, and the input is stored in the variable "radius". The "numinput" function is used for numerical inputs, and it also has parameters for setting a default value, minimum value, and maximum value.

#The "circle" function is then used to draw a circle with the specified radius. The "clearscreen" function is then used to clear the screen completely.

#The turtle shape is changed to "turtle" and the speed is set to "0" (no animation).

#A square is drawn using a for loop. The "fd" function is used to move the turtle forward and the "dot" function is used to create a green dot on each corner. The "rt" function is used to turn the turtle to the right.

#The screen is cleared again using the "clearscreen" function.

#A series of circles is drawn using another for loop. The turtle shape starts at position (300,0) and a circle is drawn using the "pendown" and "circle" functions. The "penup" function is used to pick up the pen and move it to a new position without drawing a line. The "setpos" function sets the position of the turtle shape.

#The x and y values are updated for each iteration of the loop, so that the next circle is drawn further to the right.




                                                                                                                         
 







