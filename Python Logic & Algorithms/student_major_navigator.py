# Samuel Calderon Le
# 04/26/2025
# Purpose: create an app that helps students select majors

def averageList(list):
	# Calculate the average of a list. Return number of items, total sum, and average (as a list)
	total = sum(list)
	numberOfItems = len(list)
	average = total / numberOfItems
	return([numberOfItems, total, average])

def printPopularMajors():
	# Display popular majors
	popularMajors = ["Business Administration", "Nursing", "Psychology", "Biology", "Computer Science", "Engineering", "Social Sciences", "Communications", "Education", "Visual and Performing Arts"]
	print("Here are some popular college majors:")
	for major in popularMajors:
		print(f"- {major}")

def printInfoUndeclared():
	# Print some statements about being undeclared
	print("Some students choose to be undeclared because they feel uncertain about their future career path.")
	print("However, it's beneficial to have a direction for your studies.")
	print("Fortunately, there are many resources available (like this program!) to help you better understand your interests and potential careers.")
	print("Exploring these resources would be great!")
	print("To choose a career, take into account your passions, your strengths, and your academic performance, like your GPA.")

def findMajors(subject, duration):
	# This function when given a subject and duration, it gives a list of appropriate majors which is formatted into a string

	# A nested 2D dictionary. The first key is subject; the second is duration. These 2 keys give a value which is a list of majors
	# It is very similar to a table where x is subject, y is duration and cell/value is the list. (subject, duration) --> list of majors
	majorOptions = {
		"Science": {
		"Short (4 years)": ["Biology", "Chemistry", "Physics", "Environmental Science", "Geology"],
		"Medium (6 years)": ["Physician Assistant", "Lab Manager", "Research Scientist"],
		"Long": ["University Professor (Science)", "Veterinarian"],
		},
		"Math": {
		"Short (4 years)": ["Mathematics", "Statistics"],
		"Medium (6 years)": ["Quantitative Analyst", "Data Analyst (advanced)"],
		"Long (8+ years)": ["University Professor (High Math/Stats)", "Senior Quantitative Analyst"],
		},
		"Business": {
		"Short (4 years)": ["Business Administration", "Finance", "Marketing", "Accounting"],
		"Medium (6 years)": ["Financial Manager", "Marketing Manager", "Investment Banker"],
		"Long (8+ years)": ["University Professor (Business/Econ)", "Corporate Lawyer", "Attorney", "Judge"],
		},
		"Health": {
		"Short (4 years)": ["Nurse", "Kinesiology"],
		"Medium (6 years)": ["Nurse Practitioner", "Occupational Therapist", "Epidemiologist"],
		"Long (8+ years)": ["Physician/Surgeon (many areas)", "Dentist", "University Professor (Health/Nursing)"],
		},
		"Arts": {
		"Short (4 years)": ["History", "Sociology", "Music"],
		"Medium (6 years)": ["Museum Curator", "Journalist", "Librarian"],
		"Long (8+ years)": ["University Professor (Humanities/Arts/Social Sciences)", "Archivist/Curator", "Senior Policy Advisor"],
		},
		"Technology": {
		"Short (4 years)": ["Computer Science", "IT", "Cybersecurity", "Software Engineering", "Data Science"],
		"Medium (6 years)": ["Machine Learning Engineer", "Cybersecurity Analyst (advanced)", "Robotics Engineer"],
		"Long (8+ years)": ["Lead Architect (Software/Hardware)", "Senior Data Analyst", "University Professor (Cybersecurity or other area)"],
		},
		}
	
	# Processing part; uses arguments		
	# Give a list and string of possible majors using the 2 variables above (subject, duration)
	possibleMajors = majorOptions[subject][duration]
	return(possibleMajors)


def main():
	# Main function
	
	# Lists below are options the user will choose from in the quiz
	subjects = ["Science", "Math", "Business", "Health", "Arts", "Technology"]
	durations = ["Short (4 years)", "Medium (6 years)", "Long (8+ years)"]
	
	# Prompt user to either take test or see research/info
	userInput = input("Hi, your future starts here! What do you want to do?\n (1) Take a Major Quiz, or\n (2) Learn more about Majors.\n	*Only write number in front of option in each question* ")
	
	# Option 1: Take quiz. Using 2 variables (area of interest + duration of study) to determine appropriate major
	if userInput == "1":
		print("\n~~~~~~~~~Taking Major Quiz~~~~~~~~~")
		try:
			# These 2 user inputs will be numbers. They are subtracted 1 to be used as index. The value of the index is the answer choice the user chose 
			subjectNumber = int(input("What area is the one you enjoy the most?\n 1) Science\n 2) Math\n 3) Business\n 4) Health\n 5) Arts and Culture\n 6) Technology ")) - 1
			durationNumber = int(input("For how long would you like to study?\n 1) Short (4 years)\n 2) Medium (6 years)\n 3) Long (8+ years) ")) - 1
			
			# The next 2 variables are the string/value of the index above. It is found by indexing the lists created the beginning of the main() function 
			subject = subjects[subjectNumber]
			duration = durations[durationNumber]
			
			possibleMajors = findMajors(subject, duration)
			possibleMajorsStr = ", ".join(possibleMajors)
			
			# Print results to user
			input(f"Based on your answer of choosing\n - subject as {subject}\n - duration as {duration},\n --> some possible majors for you include {possibleMajorsStr}.")
			print("Your area of interest:", subject)
			print("You would like to study for:", duration, "period of time.")
			print(f"Therefore some majors you should consider are\n	 {possibleMajorsStr}.")
		
		# Treat exceptions --> user inputted wrong number
		except Exception as e:
			print(e)
			print("... Next time, select 1-6 for subject and 1-3 for duration.")
			input("It seems you have selected an invalid response. Please choose an appropriate number for your answer. Integers 1-6 for subject, 1-3 for duration")
			print("To restart, please run the program again.")
		
	# Option 2: Print information/research
	if userInput == "2":
		print("\n~~~~~Information about Careers~~~~~")
		
		# Display Popular Majors
		printPopularMajors()
		print()

		# Talk about being undeclared
		printInfoUndeclared()
		print()

		# Calculate and display average GPA
		gpaList = [3.15, 2.77, 3.81, 1.92, 3.55, 2.49, 3.08, 3.94, 2.18, 4.00, 2.63, 3.29, 3.75, 2.91, 3.37, 1.68, 3.60, 2.05, 3.11, 2.84, 3.88, 3.42, 2.31, 3.59, 1.86, 3.02, 2.57, 3.70, 2.80, 3.45]
		gpaInfo = averageList(gpaList) # given as [numberOfItems, sum, average]
		numberOfGPA = gpaInfo[0]
		totalGPA = gpaInfo[1]
		averageGPA = gpaInfo[2]
		print("Did you know GPA is very important in choosing career paths?")
		print("Below is a sample of GPAs collected from a group of students.")
		print("GPA List:", gpaList)
		print(f"Number of GPAs: {numberOfGPA}")
		print(f"Sum of GPAs: {totalGPA:.2f}")
		print(f"Average GPA: {averageGPA:.2f}")

	
	# Print conclusion statement
	print("")
	print("~~~Thanks for using this program~~~")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	
main()