"""
Program: videoStore.py
Chapter 2 Project
7/23/2025

Simple app the prompts the user for the number of each video rental. Calculates and displays the grand total.
"""

# Variables and constants
NEW_VIDEOS = 3.0
OLD_VIDEOS = 2.0

# Input phase
numNew = int(input("Please enter the number of NEW videos being rented >>"))
numOld = int(input("Next, enter the number of OLD videos being rented >>"))

# Processing phase
grandTotal = (NEW_VIDEOS * numNew) + (OLD_VIDEOS * numOld)
grandTotal = round(grandTotal, 2)

# Output phase
print("The customer is renting: " + str(numNew) + "new video(s).")
print("The customer is also renting " + str(numOld) + " old video(s).")
print("The total charge is: $" + str(grandTotal))

input("\nPress Enter to quit the program")