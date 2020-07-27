import turtle
import math
import time

squares = turtle.Turtle() #initializing two turtles to draw simultaneously
spiral = turtle.Turtle()  #the squares and the spiral
squares.color("blue")
spiral.color("red")

base1 = 0      #base numers to start the fibonacci's sequence 
base2 = 1
fibonacci = 1

factor = 1  #increase the factor to draw bigger squares and spiral, decrease to reduce 

max = input("How many squares do you want?") #max is the number of steps of the sequence
time.sleep(3)

for i in range(int(max)):
   print(str(i+1)+". "+str(fibonacci))
   
   for f in range(6):       #drawing the squares
       squares.forward(fibonacci * factor)
       if f<5:
        squares.right(90)
 
   fwdw = math.pi * base2 * factor / 2  #calculating the circumference for each square
   fwdw /= 90
   spiral.speed(100)
   for j in range(90):  #drawing a quarter of the circumference to compose the spiral
       spiral.fd(fwdw)
       spiral.rt(1)
   
   fibonacci = base2 + base1  #going on with fibonacci's sequence
   base1 = base2
   base2 = fibonacci
   

turtle.exitonclick()   #keep the window open, left click will close the window 
