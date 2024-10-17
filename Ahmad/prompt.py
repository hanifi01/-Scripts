
input = input("How odl are you?:")

if input.isdigit():
    age = int(input)
    print("You will be", age + 1, "years old next year")

else:
    print ("Invalid entry: you must enteer numeric value")
    exit