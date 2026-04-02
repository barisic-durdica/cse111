import csv

def read_dictionary(filename, key_column_index):
    s_dictionary={}
    with open(filename, "rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        for row in csvreader:
            key_value = row[key_column_index]
            s_dictionary[key_value] = row
    return s_dictionary

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary("students.csv", KEY_INDEX)
    inumber = input("Please enter an I-number: ")
    inumber = inumber.replace("-","")
    if not inumber.isdigit():
        print("Invalid I-number.")
    elif len(inumber) != 9:
        print("An I-number must be 9 digits long")

    if inumber in students:

        student = students[inumber]
        name = student[NAME_INDEX]
        print(f"The student's name is {name}")
    else:
        print("No such student!")
    


if __name__ == "__main__":
    main()