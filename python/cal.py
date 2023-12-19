# num1 = float(input("Enter Number 1: - "))
# op = input("Enter Operator; - ")
# num2 = float(input("Enter number 2: - "))

# if op == "+":
#     print("Sum:", num1 + num2)
# elif op == "-":
#     print("Diffrence:", num1 - num2)
# elif op == "/":
#     print("Division:", num1 / num2)
# elif op == "*":
#     print("Multiplication:", num1 * num2)
# else:
#     print("Wrong Operator")

# while True:
    
#     num1 = float(input ("Enter Number1:"))
#     op = input("Enter oiprator:")
#     num2 = float(input("Enter number 2:"))
#     # while loop - for loop

#     if op == "+":
#         print("Sum:", num1 + num2)
#     elif op == "-":
#         print("Diffrence:", num1 - num2)
#     elif op == "/":
#         print("Division:", num1 / num2)
#     elif op == "*":
#         print("Multiplication:", num1 * num2)
#     else:
#         print("Wrong operator")

while True:
    expression = input("") #2+4

    num1 = int(expression[0])
    op = expression[1]
    num2 = int(expression[2])

    if op == "+":
        print("Sum:", num1 + num2)
    elif op == "-":
        print("Diffrence:", num1 - num2)
    elif op == "/":
        print("Division:", num1 / num2)
    elif op == "*":
        print("Multiplication:", num1 * num2)
    else:
        print("Wrong operator")
