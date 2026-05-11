# Samuel Calderon Le
# 09/23/2022
# Purpose: drawing the night sky

import turtle

# Create a function of drawing a star
def drawStar(t, col, rad, x, y):
	# Go to given coordinates and set color
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.color(col)

	# Draw the star
	for i in range(4):
		t.circle(rad, 90)
		t.right(180)

# Create a function of drawing a cloud
def drawCloud(t, col, rad, x, y):
	# Go to given coordinates and set color
	t.penup()
	t.setpos(x,y)
	t.pendown()
	t.color(col)
	
	# Draw cloud by circles
	for i in range(3):
		t.pendown()
		t.begin_fill()
		t.circle(rad)
		t.end_fill()
		t.penup()
		t.forward(rad)
		
def main():
	
	print("The Starry Night")
	
	t = turtle.Turtle()
	screen = turtle.Screen()
	screen.bgcolor("midnightBlue")
	t.speed(10)
	
	#Draw the moon
	t.penup()
	t.setpos(-80, 0)
	t.pendown()
	t.color("beige")
	t.begin_fill()
	t.circle(100)
	t.end_fill()
	
	#Draw a cloud
	drawCloud(t, "lightCoral", 50, -50, -20)

	
	#Draw the stars
	drawStar(t, "gold", 20, 100, 10)
	drawStar(t, "gold1", 10, 0, -100)
	drawStar(t, "khaki", 30, 100, 100)
	drawStar(t, "gold4", 15, -100, -50)
	drawStar(t, "goldenrod", 30, 20, -70)
	drawStar(t, "LightGoldenrod", 5, 100, -100)
	drawStar(t, "LightGoldenrod", 18, 120, -160)
	drawStar(t, "LightGoldenrod", 26, -120, -120)
	#drawStar(t, "LightGoldenrod", 13.998, -72, 32)
	
main()
