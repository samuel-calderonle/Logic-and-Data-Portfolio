# Samuel Calderon Le
# 02/17/2025
# Purpose: create a quiz that will help determine a client's appropriate clothes for vacation

def main():
    # Print store description
    print("Welcome to Timeless Threads! Here we provide a variety of clothing for every vacation.")
    print("Discover your next attire with just a few questions!")
    input("Welcome to Timeless Threads!\n    Discover the apparel you need in your next vacation with just a few questions!")
    
    # This is a dictionary of possible destinations and weather types
    possibleDestinations = {
        "Spain": "hybrid",
        "Cuba": "warm",
        "Canada": "hybrid",
        "Russia": "cold",
        "Maldives": "warm",
        "Mexico": "hybrid",
        "Peru": "hybrid",
        "Australia": "hybrid"
    }

    # Ask user questions
    name = input("What is your name? ")
    destination_list = "\n".join(possibleDestinations.keys())
    destination = input(f"{name}, where will you be going? We have some suggestions below:\n{destination_list}\n")
    destination = destination.strip().capitalize() 

    # Validate season input
    season = input("That is an awesome destination! What season will you be there? (summer/fall/winter/spring) ").lower()
    while season not in ["summer", "fall", "winter", "spring"]:
        print("Please provide a valid season (summer, fall, winter, spring).")
        season = input("What season will you be going on there? (summer/fall/winter/spring) ").lower()
        
    color = input("Lastly, what is your favorite color? ").lower().capitalize()
    
    # Determine if the weather will be cold or warm
    if destination not in possibleDestinations:
        while True:
            try:
                weather = input("It seems that we cannot determine the weather of your destination. Would you tell us if it will be cold or warm? ").strip().lower()
                if weather not in ["cold", "warm"]:
                    raise Exception("Invalid input. Please enter 'cold' or 'warm'.")
                break
            except Exception as e:
                print(e)
    else:
        characteristic = possibleDestinations[destination] 
        if characteristic == "cold" or characteristic == "warm":
            weather = characteristic
        elif characteristic == "hybrid": 
            if season == "spring" or season == "summer":
                weather = "warm"
            else:
                weather = "cold"
        else:
            weather = "warm" 
    
    # Determine appropriate clothing based on weather
    if weather == "cold":
        clothes = ["Cap", "Insulated Jacket", "Snow Pants", "Gloves", "Woolen Socks"]
    else:
        clothes = ["Hat", "T-shirt", "Shorts", "Sandals", "Slippers", "Sunglasses"]
        
    # Add favorite color prefix
    for i in range(len(clothes)):
        clothes[i] = f"{color} {clothes[i]}"

    # Output the results
    print("\n" + "~" * 52)
    print(f"{name}, you indicated that you would like to travel to {destination}.")
    print(f"Your favorite color is {color.lower()}, and you are going in the {season}.")
    print("We have the perfect outfit for you:")
    for item in clothes:
        print(f"- {item}")
    print("Enjoy your trip!")
    print("~" * 52)

if __name__ == "__main__":
    main()
