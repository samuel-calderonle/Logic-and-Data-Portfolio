#Samuel Calderon Le
#02/26/25
#Purpose: create a text-based game which the players pick up items
import random

def main():
	
	#Print description
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("Welcome to Forgotten Fortress!")
	print("No one has gone here for some time, and treasure might await...")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	input("Some mystery might await...")

	#Create a list which will be used later to randomly choose items the user will pick up
	itemsList = ["TREASURE CHEST", "box", "crown", "paper", "shoe", "cup", "lamp", "pencil", "radio"]
	totalScore = 0
	itemsPickedUp = []
	
	#Ask user to pick up items
	for i in range(3):
		item = random.choice(itemsList)
		userInput = input(f"You are walking and find a {item}. Would you like to pick it up? (y/n) ").lower()[0]
		if userInput == "y":
			print(f"You have picked up {item}. You gained one point!")
			totalScore += 1
			itemsPickedUp.append(" " + item)
		elif userInput == "n":
			print(f"You did not pick up the item.")
		elif userInput == "q":
			break
		else:
			print("It seems that you neither chose yes or no. Type 'y' or 'n' next time.")
			continue

	print(f"\nYour total score for this game is {str(totalScore)}!")
	print(f"During your journey, you picked up {itemsPickedUp}. I hope you come back again soon!\n")

main()

while input("Would you like to play again? (y/n) ").lower()[0] == "y":
	try:
	  times = input("How many more times would you like to play? ")
	  for i in range(int(times)):
		  main()
	except Error:
		print("It seems that you did not input an integer to play again.")