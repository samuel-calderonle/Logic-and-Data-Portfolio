# Can you guess the secret message?
# Samuel Calderon
# 10/07/2024
# Purpose: the user has to guess what the secret message is

def main():

	#Create secret message and its ASCII equivalent
	secretMessage = "To be or not to be"
	secretMessageASCII = []
	
	for i in range(len(secretMessage)):
		secretMessageASCII.append(ord(secretMessage[i]))

	#print(secretMessage, "\n", secretMessageASCII)

	#Ask the user to guess the message
	guessCorrect = True if(str(input("Guess the secret message: (it's in ASCII, 32 is a space and 111 is an 'o') \n " + str(secretMessageASCII) + " ")) == secretMessage) else False
	#print(guessCorrect)
	secretMessage = ""
	for i in range(len(secretMessageASCII)):
		secretMessage += chr(secretMessageASCII[i])
	
	#Display the encoded, decoded message + if they got it correct or not
	print("The encoded message:")
	print(secretMessageASCII)
	print("")
	print(("You guessed it right!" if guessCorrect else "You got it wrong.") + " The correct answer is:")
	print(secretMessage)
	
main()
