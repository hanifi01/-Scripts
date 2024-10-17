
input = input("How old are you?:")

if input.isdigit():
    age = int(input)
    print("You will be", age + 1, "years old next year")
    if age >= 18:
        print("You are eligible to drink (coffee)!", end="")
    else:
        print("You are too young to drink (coffee), young person!", end="")
else:
    print("Invalid entry: you must enter a numeric value")