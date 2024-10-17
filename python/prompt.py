name= input(" what is your name?:")
input = input("How old are you?:")

if not name.isdigit():
    print("Hello there", name, end=":\n")

else:
    print ("erros: invalid entry. you must enter alphabetical value")

if input.isdigit():
    age = int(input)
    print("You will be", age + 1, "years old next year")
    if age >= 18:
        print("You are eligible to drink (coffee)!", end="!\n")
    else:
        print("You are too young to drink (coffee), young person!", end="!\n")
else:
    print("Invalid entry: you must enter a numeric value")
