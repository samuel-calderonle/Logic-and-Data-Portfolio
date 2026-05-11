# Samuel Calderon Le
# 09/11/2024
# Purpose: find the volume and surface area of a sphere

from math import*

def main():

    # Displays context
    print("Isai is a fan of all sports, and it is his top choice when he has free time.")
    print("Out of curiosity, Isai wants to calculate a ball's volume and surface area.")
    print()
    print("He needs your help by providing the name of the ball and its radius.")
    print()
    
    # Asks user to input ball's name and radius. Also stores these values
    ballName = input("Which ball should he research about first? ")
    ballRad = float(input("A " + ballName + " is a great choice! He thanks you. He just needs one more thing to do calculations. He would like the radius of the " + ballName + ". (The unit for the answer must be cm (and please don't include 'cm')). "))
    #print(ballName + " is " + str(ballRad) + "cm in radius.")
    
    # The ball's S Area and Volume will be calculated
    ballSA = round((4 * pi * pow(ballRad, 2)), 2)
    ballVol = round(4.0/3.0 * pi * pow(ballRad, 3), 2)
    #print(ballSA, ballVol)
    
    # Displays the answers and end program
    print("Thanks for your help! He has done all the calculations.")
    print()
    print("The " + ballName + ", with a radius of " + str(ballRad) + " cm,")
    print("has a surface area of " + str(ballSA) + " cm squared")
    print("and a volume of " + str(ballVol) + " cm cubed!")
    print()
    print("Thanks to you, Isai now knows the surface area and the volume of a " + ballName + ".")

    
main()
