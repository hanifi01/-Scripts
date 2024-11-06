import inquirer

question = [
    inquirer.List('operator',
                  message="Please choose an operator:",
                  choices=["+", "*", "/", "//", "**","-"],
                  default="+"),
    inquirer.Text("num1", message="Enter first number:"),
    inquirer.Text("num2", message="Enter second number:"),
]



answers = inquirer.prompt(question)
if answers['operator'] == '+':
    result = int(answers['num1']) + int(answers['num2'])
    print("Answer:", result)


if answers['operator'] == '*':
    result = int(answers['num1']) * int(answers['num2'])
    print("Answer:", result)

if answers['operator'] == '/':
    result = int(answers['num1']) / int(answers['num2'])
    print("Answer:", result)


if answers['operator'] == '-':
    result = int(answers['num1']) - int(answers['num2'])
    print("Answer:", result)



