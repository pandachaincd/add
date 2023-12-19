def calculator():
    while True:
        expression = input("")
        num1 = int(expression[0])
        op = expression[1]
        num2 = int(expression[2])

        if op == "+":
            print("sum:", num1 + num2)
        elif op == "-":    
            print( "Diffrence:", num1 - num2)
        elif op == "/": 
            print("Division:", num1 / num2)
        elif op == "*":
            print("Multiplication:", num1 * num2)


# program = input("Enter a Program: - ")

# if program == "calculator":
#     calculator()

# ---------------------------------------------------------------

employee = [
    ["teka", 1234, 100000, "+25194762376"],
    ["yared", 2345, 29090, "+25189445389"]
]
print(employee[0][0])

# name = input("Enter name:- ")
# for i in employee:
#     if name == i[0]:
#         print(i)

def update():
    name = input("Enter name:- ")
    for i in employee:
        if name == i[0]:
            correct = int(input("Please enter What to update: - \n"
                            "1 - Name \n"
                            "2 - Id \n"
                            "3 - Salary \n"
                            "4 - Phone Number \n"))
            if correct == 1:
                updated_name = input("Enter name: - ")
                employee[0][0] = updated_name
                print("Here is the updated data!!")
                print(i)


    def add_employee():
