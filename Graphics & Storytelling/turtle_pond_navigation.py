
# 09/25/2024
# Samuel Calderon Le
# Challenge: move turtle into the pond

import turtle

from random import *

from math import *

userT = turtle.Turtle()
computerT = turtle.Turtle()

# Start main function
def main():

	# Configure user's turtle
	userT.shape("turtle")
	userT.color("forestGreen")
	userT.penup()
	userT.setpos(-65,-10)
	userT.setheading(360*random())
	userT.pendown()
	
	print("Try to move the turtle into the pond.")
	
	# Configure turtle that will draw the pond
	computerT.penup()
	computerT.hideturtle()
	computerT.setpos(80,35)
	computerT.pendown()
	computerT.color("blue")
	computerT.speed(0)
	
	
	# Show menu of moves
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("~ Menu of Turtle Moves      ~")
	print("~ F: Move Forward           ~")
	print("~ B: Move Backwards         ~")
	print("~ L: Turn Left              ~")
	print("~ LL: Turn Sharp Left       ~")
	print("~ R: Turn Right             ~")
	print("~ RR: Turn Sharp Right      ~")
	print("~ Q: Quit                   ~")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


	# Draw the pond
	for i in range(34):
		computerT.forward(100)
		computerT.left(107)
	computerT.forward(49)
	computerT.color("DeepSkyBlue")
	
	# Finding pond's center + radius to later on know whether the turtle is inside
	# To find center, used two opposite points across the circle, then find their midpoint
	computerT.begin_fill()
	radius = 37
	computerT.circle(radius, 180)
	xCor1 = computerT.xcor()
	yCor1 = computerT.ycor()
	computerT.circle(radius, 180)
	xCor2 = computerT.xcor()
	yCor2 = computerT.ycor()
	centerX = (xCor1 + xCor2)/2
	centerY = (yCor1 + yCor2)/2
	#radius = (sqrt(pow((xCor1 - xCor2), 2) + pow((yCor1 - yCor2), 2)))/2
	#print(centerX, centerY, radius)
	
	# Prompt user to move turtle
	
	choice = ""
	
	while(choice != "Q"):
		choice = input("How should you move the turtle next? (F, B, L, LL, R, or RR). Q to quit program.")
		
		if (choice == "F"):
			userT.forward(50)
			userT.stamp()
		elif (choice == "B"):
			userT.backward(20)
			userT.stamp()
		elif (choice == "L"):
			userT.left(50)
		elif (choice == "LL"):
			userT.left(110)
		elif (choice == "R"):
			userT.right(50)
		elif (choice == "RR"):
			userT.right(110)
			
		# Check if user won using distance formula
		if (sqrt(pow((userT.xcor() - centerX), 2) + pow((userT.ycor() - centerY), 2)) <= radius):
			input("You have won the game! Thanks for playing. See you soon!")
			print("You have won the game!")
			choice = "Q"
		
		#print(userT.pos(), userT.xcor(), userT.ycor())
		
	print("Thanks for playing. See you soon!")
	
main()
