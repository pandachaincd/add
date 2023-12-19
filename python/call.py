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
                    # 0                     1
            # 0        1    2
company = [["teka", 1234, 10000], ["yared", 4321, 12345]]

# employee1 = []
# name = input("What is Your name: - ")
# id = int(input("What is the id: - "))
# salary = int(input("What is your salary: -"))         

# employee1.append(name)
# employee1.append(id)
# employee1.append(salary)

# company.append(employee1)
# print(company)

# print(company[0][1])

# name = input("Name: -").lower()
# if (name == "yared"):
#     id = int(input("Id value: - "))
#     company[1][1] = id
#     print(company)
# elif (name == "teka"):
#     id = int(input("Id value: - "))
#     company[0][1] = id
#     print(company)

# name = input ("Name : -")
# if(name == "yared"):
#     id = int(input("ID value: -"))
#     company[1][1] = id 
#     print(company)

print(company)



