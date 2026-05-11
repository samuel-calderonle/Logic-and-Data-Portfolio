# Making a Sunset
# Samuel Calderon
# 09/19/2024
# Purpose: make a lovely pattern

import turtle

def main():

	darwin = turtle.Turtle()
	darwin.penup()
	darwin.setpos(100,-100)
	darwin.pendown()
	darwin.left(87)
	darwin.speed(0)
	
	colors = ["yellow", "gold", "#e8c979"]
	
	print("This is the sunset:")
	
	for i in range(3):
		darwin.color(colors[i])
		for j in range(60):
			darwin.forward(200)
			darwin.left(90.5)
		
		print("We are " + str(i + 1) + "/3 way through!")
	
	print("We are done!!")
	darwin.hideturtle()

main()