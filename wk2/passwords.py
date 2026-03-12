"""
Author: Durdica Barisic

Purpose: Practice Functions - Project Passwords
"""

# To exceed requirements for this project I added a code that tracks how many passwords the user tests before 
# quitting the program. At the end, the program tells you the total number of passwords tested.

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive = False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if case_sensitive:
                if word == line:
                    return True
            else:
                if word.lower() == line.lower():
                    return True
    
    return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
        
    return False

def word_complexity(word):
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    
    if word_has_character(word, UPPER):
        complexity += 1
    
    if word_has_character(word, DIGITS):
        complexity += 1
    
    if word_has_character(word, SPECIAL):
        complexity += 1
    
    return complexity

def password_strength(password, min_length = 10, strong_length = 16):

    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    complexity = word_complexity(password)

    strength = 1 + complexity
    return strength
    

def main():

    count = 0

    while True:
        password = input("Enter a password to test (or q to quit): ")

        if password == "q" or password == "Q":
            print(f"You tested {count} password(s).")
            break

        strength = password_strength(password)

        print(f"Password strenght: {strength}")

        count += 1
            

if __name__ == "__main__":
    main()