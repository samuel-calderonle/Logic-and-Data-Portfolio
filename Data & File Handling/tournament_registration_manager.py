# Samuel Calderon Le
# 04/08/2024
# Purpose: read a CSV file of pre-registered players and provide options

import csv

def main():
    # Lists that will contain information from CSV file
    avatarName = []
    playerName = []
    playerNumber = []
    hometown = []
    
    # Read CSV and copy it to lists
    try:
        with open("battle_royale.csv", mode="r") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if len(row) >= 4:
                    avatarName.append(row[0])
                    playerName.append(row[1])
                    playerNumber.append(row[2])
                    hometown.append(row[3])
    except FileNotFoundError:
        print("Error: 'battle_royale.csv' not found.")
        return

    # Print information about program
    print("Welcome to Battle Royale!")
    print("Game Tournament Registration\n")

    while True:
        print("~~~~~~~~~ Main Menu ~~~~~~~~~")
        print("1. Find a pre-registered player")
        print("2. Find the number of a specific player")
        print("3. Print list of players")
        print("4. Quit/Log out")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        choice = input("Enter choice (1-4): ").strip()
        found = False

        # Option 1: Find a pre-registered player
        if choice == "1":
            search_name = input("What player name do you want to search? ").strip().capitalize()
            print("Looking for a player ...\n")
            
            for i in range(len(playerName)):
                if playerName[i].capitalize() == search_name:
                    found = True
                    print(f"{playerName[i]} is in the list of pre-registered players")
                    print(f"Data: {[avatarName[i], playerName[i], playerNumber[i], hometown[i]]}\n")
            
            if not found:
                print(f"It seems that {search_name} was not found.\n")
        
        # Option 2: Find a player number
        elif choice == "2":
            search_name = input("What player's number do you want to find? ").strip().capitalize()
            print("Searching for a player's number ...")
            
            for i in range(len(playerName)):
                if playerName[i].capitalize() == search_name:
                    found = True
                    print(f"{playerName[i]}'s number is {playerNumber[i]}!\n")
            
            if not found:
                print(f"It seems that {search_name} was not found in the list.\n")
                    
        # Option 3: Print the list of players
        elif choice == "3":
            print("Printing out player list ...")
            for i in range(len(avatarName)):
                print([avatarName[i], playerName[i], playerNumber[i], hometown[i]])
            print("")
                
        # Option 4: Quit / Logout
        elif choice == "4":
            print("Terminating program ...")
            break
            
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.\n")
    
    print("~~~~~~~~~ PROGRAM TERMINATED ~~~~~~~~~")

if __name__ == "__main__":
    main()
