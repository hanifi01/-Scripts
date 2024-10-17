# grading system: write a program that takes a number input (0-100
# convert the user and prints a grade suing the following system:
# A: 90 -100
# B:80-89
# C:70-79
# D:60-69
# F: below 60




grade = input("What's your score?: ")


if grade.isdigit():
    grade = int(grade)
    
    
    if 0 <= grade <= 100:
        if grade >= 90:
            print("Your grade: A")
        elif grade >= 80:
            print("Your grade: B")
        elif grade >= 70:
            print("Your grade: C")
        elif grade >= 60:
            print("Your grade: D")
        else:
            print("Your grade: F")
    else:
        print("Error: Invalid entry, you must enter a number between 0-100")
else:
    print("Error: Invalid entry, you must enter a numeric value")