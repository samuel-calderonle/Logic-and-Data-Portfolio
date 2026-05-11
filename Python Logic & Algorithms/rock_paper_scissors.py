import random

def randomRPS():
        return random.choice(["R", "P", "S"])

def resultRPS(player1, player2):
        # 0 means draw, 1 means first one, -1 means second one    
        if (player1 == player2):
                return 0
        if (player1 == "R"):
                if (player2 == "S"):
                        return 1
                else:
                        return -1
        if (player1 == "P"):
                if (player2 == "R"):
                        return 1
                else:
                        return -1
        if (player1 == "S"):
                if (player2 == "P"):
                        return 1
                else:
                        return -1

def main():
        userInput = compChoice = ""
        gameNumber = gamesWon = gamesLost = gamesDrawn = score = result = 0

        print("Hey! Let's play a game of Rock, Paper, Scissors! Choose [R]ock, [P]aper, or [S]cissors. Type [Q]uit to quit.")
        
        while True:
                userInput = input("Choose [R]ock, [P]aper, or [S]cissors. Type [Q]uit to quit: ")
                compChoice = randomRPS()  # Computer randomly chooses Rock, Paper, or Scissors

                if (userInput == "Q"):  # Quit condition
                        break

                if userInput not in ["R", "P", "S"]:  # Invalid input condition
                        print("Invalid input, try again!")
                        continue

                result = resultRPS(userInput, compChoice)
                gameNumber += 1
                score += result

                # Using the `%` formatting
                print("\nGame %d:" % gameNumber)
                print("You chose: %s" % userInput)
                print("The computer chose: %s" % compChoice)
                
                if (result == 1):
                        print("You won this round!")
                        gamesWon += 1
                elif (result == -1):
                        print("You lost this round.")
                        gamesLost += 1
                elif (result == 0):
                        print("It's a tie!")
                        gamesDrawn += 1

        # Final output using `%` formatting
        print("\nGame Over! You won %d games, lost %d games, and drew %d games. Final score: %d" % (gamesWon, gamesLost, gamesDrawn, score))

# Start the game
main()
