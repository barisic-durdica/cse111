# 1. Open the file for reading
with open("provinces.txt", "r") as file:
    # 2. Read lines into a list (strip removes \n)
    provinces = [line.strip() for line in file]

# 3. Print the entire list
print(provinces)

# 4. Remove the first element
provinces.pop(0)

# 5. Remove the last element
provinces.pop()

# 6. Replace "AB" with "Alberta"
for i in range(len(provinces)):
    if provinces[i] == "AB":
        provinces[i] = "Alberta"

# 7. Count how many times "Alberta" appears
count = provinces.count("Alberta")

# Print result
print(f"Alberta occurs {count} times in the modified list.")