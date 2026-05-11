# Chess Club Application Form
# By: Samuel C. (President)
# 09/29/2024

def application():
	
	# Talk about us
	print("APPLICATION FOR CHESS CLUB")
	print("")
	print("About Us:")
	print("Founded in 2025, we are dedicated to play and improve the game of chess.")
	print("Additionally, we have a large community where we have monthly tournaments within the school and a district-wide competition.")
	print("Join us today!")
	
	# Ask user's info
	name = input("Hi, there! It seems that you want to join this high school's chess club. First of all, what's your name? ")
	age = int(input("What is your age? "))
	dedication = input("So, " + name + ", are you dedicated and have a passion for playing chess? ")
	chessLevel = input("What is your chess level (New to Chess, Beginner, Intermediate, Advanced, Master)? Don't be ashamed if you are a novice. ")
	availability = input("We will be meeting each Thursday during lunch in the library. Will you be available? ")
	compete = input("Last question: Are you interested and want to compete against other schools? (Will occur some time in April). ")
	
	# Change some values into boolean (y/n ==> true/false)
	if(dedication[0] == "n" or dedication[0] == "N"):
		dedication = ""
	if(availability[0] == "n" or availability[0] == "N"):
		availability = ""
	if(compete[0] == "n" or compete[0] == "N"):
		compete = ""
	dedication = bool(dedication)
	availability = bool(availability)
	compete = bool(compete)
	#print(name, age, dedication, chessLevel, availability, compete)
	
	# Print user's responses
	print("")
	print("Thank you for filling out the form, " + name + ".")
	print("")
	print("Your application replies are:")
	print("Age: " + str(age))
	print("Dedicated: " + ("Yes" if dedication == True else "No"))
	print("Chess Level: " + chessLevel)
	print("Able to join us during lunch: " + ("Yes" if availability == True else "No"))
	print("Competing: " + ("Yes" if compete == True else "No"))
	print("")
	
	# Determine if accepted + print results
	if (age <= 19 and dedication == True and availability == True):
		print("Welcome! You have been accepted to this chess club. Meet us this Thurday for more info.")
		if (compete == True):
			print("We also thank you for wanting to compete against other schools. We are certain to win this year!")
		else:
			print("Although you cannot go to the district-wide tournament, we will still have competitions in school. We await your participation!")
	else:
		print("Although we want you with us, it seems you are not eligible.")
		if (age > 19):
			print("You are an adult! This club is for high school students.")
		elif (dedication == False):
			print("We cannot accept you due to your lack of commitment.")
		elif (availability == False):
			print("Because you cannot join us on Thursday, you are not part of the club. Join us next year :)")
	
application()
