# Samuel Calderon Le
# 04/05/2025
# Purpose: search for sunrise time for 5k run

import csv

def main():
    # 1. Print description (Cleaned up for flow)
    print("Welcome to 5K for Charity! We are excited to have you.")
    print("We are dedicated to helping those in poverty.")
    print("Our next race will be during sunrise.\n")
    
    # 2. Setup variables
    found = False
    information = []

    # 3. Ask the user for the time
    time_input = input("Please enter a sunrise time to search for (Format H:MM): ").strip()
		
    # 4. Open and search (Crucial: Keep everything inside the 'with' block)
    try:
        with open("sun_data.csv", mode="r") as file:
            dataset = csv.reader(file, delimiter=',')
            
            for row in dataset:
                # row[1] is the time column. .strip() removes hidden spaces.
                if len(row) > 1 and row[1].strip() == time_input:
                    found = True
                    information = row
                    break 
    except FileNotFoundError:
        print("Error: 'sun_data.csv' not found. Put it in the same folder as this script.")
        return

    # 5. Results
    if found:
        print(f"\nSunrise time found: {information[1]}")
        print(f"The date will be {information[0]}")
        
        # Confirmation
        run_choice = input(f"Would you like to run on {information[0]} at {information[2]}? (yes/no): ").lower()
		
        if run_choice == "yes":
            print("\nGreat! Registration confirmed.")
            print(f"Location: {information[2]}")
            print("We hope to see you there!")
    else:
        print(f"Sorry, the time {time_input} was not found in our sunrise data.")

if __name__ == "__main__":
    main()
