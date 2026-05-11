# Samuel Calderon Le
# Date: 2/11/2025
# Purpose: Write a program for buying at a shop

def main():
    # Print shop's information
    print("Welcome to Animal Clothes Shop! \n**Today, anyone with a purchase above or at $200 will earn a $20 gift card**")
    print("We provide a variety of items. From Shark Shorts to Zebra Zip-ups.\n")
    
    # Ask user how much they would like to spend. Round that number to the nearest hundredth
    while True:
        try:
            amountToSpend = input("How much money would you like to spend today? ")
            amountToSpend = round(float(amountToSpend), 2)
            if amountToSpend < 0:
                raise Exception("Amount of money willing to spend must be positive.")
            else:
                print(f"You plan to spend ${amountToSpend}.\n")
                break
        except ValueError:
            print(f"Please enter a positive decimal or integer.")
        except Exception as e:
            print(f"Please enter a valid positive number. Error: {e}")
    
    # Create shop items
    checkout = False
    totalCost = 0
    selectedItems = []
    shopItems = {
        "Shark Shorts": 15.21,
        "Zebra Zip-up": 31.89,
        "Dolphin Dress": 57.28,
        "Monkey Mittens": 8.76,
        "Bearlike Boots": 48.08,
        "Shellfish Shoes": 62.82,
        "Lynx Leggings": 12.23,
        "Tiger T-shirt": 17.63,
        "Giraffe Gloves": 13.58,
    }
    
    stringShopItems = "~~~~~~~~Store Options:~~~~~~~~~~\n"
    for index, (key, value) in enumerate(shopItems.items()):
        stringShopItems += f"    {(index + 1)}.  {key}:  ${value}\n"
    
    # Main shopping time
    while not checkout:
        totalCost = round(totalCost, 2)

        # Generate a recommendation
        recommendation = "No recommendation available."
        if amountToSpend > totalCost:
            for item, price in shopItems.items():
                if price <= (amountToSpend - totalCost):
                    recommendation = f"{item} for ${price}"
                    break
        
        # Determine if the user has reached the $200 mark
        gift = totalCost >= 200
        
        if gift:
            stringGift = "Woo-Hoo! Your purchase is above $200. You earned a $20 gift card!"
        else:
            stringGift = f"**Spend ${round(200-totalCost, 2)} more to earn a $20 gift card.**"
        
        print(f"\n{stringShopItems}")
        print(f"Total Amount Spent: ${totalCost}")
        print(f"Budget Remaining: ${round(amountToSpend - totalCost, 2)}")
        print(f"Recommendation: {recommendation}")
        print(f"Items in cart: {selectedItems}")
        print(stringGift)
        
        userInput = input("\n-- Enter 1-9 to add to cart, or 'ch' to checkout: ").strip().lower()
        
        if userInput == "ch":
            checkout = True
        else:
            try:
                choice = int(userInput) - 1
                if 0 <= choice < len(shopItems):
                    itemName = list(shopItems.keys())[choice]
                    itemPrice = list(shopItems.values())[choice]
                    
                    selectedItems.append(f"{itemName} (${itemPrice})")
                    totalCost += itemPrice
                    print(f"\n>>> Added {itemName} to cart!")
                else:
                    print("\n!!! Please select a valid number (1-9).")
            except ValueError:
                print("\n!!! Invalid input. Enter a number or 'ch'.")

    # Final checkout message
    print("\n" + "="*30)
    print("      CHECKOUT SUMMARY")
    print("="*30)
    for item in selectedItems:
        print(f"- {item}")
    print("-" * 30)
    print(f"TOTAL: ${round(totalCost, 2)}")
    
    if gift:
        print("BONUS: You earned a $20 gift card!")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
