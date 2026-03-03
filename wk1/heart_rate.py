"""
Author: Durdica Barisic

Purpose: Write a Python program that gets input from a user, uses variables, performs arithmetic, and displays results for the user to see
"""

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("Please enter your age: "))

max_heart_rate = 220 - age

min = max_heart_rate * 0.65
max = max_heart_rate * 0.85

print("When you exercise to strengthen your heart, you should") 
print(f"keep your heart rate between {int(min)} and {int(max)} beats per minute.")