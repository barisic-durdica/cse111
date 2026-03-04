"""
Author: Durdica Barisic

Purpose: Write a program that will accept user input that describes a tire then calculate and display the tire's volume.
"""

# Enhancement: The program asks the user if they want to buy tires.
# If the user says yes, then the program will ask for their phone number and save it in volumes.txt.
# If the user says no, the program says thank you and have a nice day.

import math
from datetime import datetime

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000 

print(f"The approximate volume is {volume:.2f} liters")

buy = input("Do you want to buy the tires? (yes/no): ")

phone = ""

if buy.lower() == "yes":
    phone = input("Enter your phone number: ")
else:
    print("Thank you, have a nice day!")

current_date = datetime.now()

with open("volumes.txt", "at") as file:
    print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}", file=file)

