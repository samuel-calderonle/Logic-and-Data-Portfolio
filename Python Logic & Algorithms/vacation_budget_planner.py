# Samuel Calderon Le
# 9/17/2024
# Purpose: Calculate a mini vacation

def main():

	#Ask user for CITY, PEOPLE AMOUNT, AIRFARE, OTHER COSTS
	city = input("It is time for a mini-vacation this weekend (2 days and 1 night)! We can help you plan this experience. Where do you want to go? ")
	peopleAmt = int(input("WOW! That's a great choice! My family wants to go to " + city + " next summer. You will have a nice time there. By the way, how many people do you think will go with you? ")) + 1
	airfare1Person = float(input("Ok. We have done a couple calculations, but we don't know how much the plane ticket will cost. Will you help us? Please tell us how much is the airfare (in round trip and per person). "))
	tourism1Person = float(input("Thanks! Almost everything is set. As for the last thing, please include any extra expenses and any tourism costs (like visiting a museum). "))
	#print(city, peopleAmt, airfare1Person, tourism1Person)
	
	#Calculate each individual item/expense
	airfare = airfare1Person * peopleAmt
	food = 135.99 * peopleAmt
	transportation = 10.99 * peopleAmt
	tourism = tourism1Person * peopleAmt
	lodging = 129.99 + 57.89 * (peopleAmt - 1)
	total = airfare + food + transportation + tourism + lodging
	#print(airfare, food, transportation, tourism, lodging, total)

	#Display results
	print("It is time for a mini-vacation!")
	print("")
	print("Your vacation expenses to " + city + ".")
	print("")
	print("Items			Cost")
	print("Flight:          $" + str(airfare))
	print("Tourism:         $" + str(tourism))
	print("Hotel:           $" + str(lodging))
	print("Meals:           $" + str(food))
	print("Transportation:  $" + str(transportation))
	print("-----~-------|-------~-----")
	print("Total:           $" + str(total))
	print("")
	print("Enjoy your trip!")

	
main()