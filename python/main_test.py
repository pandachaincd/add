import time
database = [["teka", 1234, 100000, "+25194762376"],]

def create_employee():
    employee = []
    print("\n\tCreatin An Employee \n"
          "\tPlease enter the following Information\n")
    name = input("Enter Name:- ")
    age = int(input("Enter age :-"))
    salary = int(input("Enter salary:-"))
    id = int(input("Enter id:-"))
while True:
            try:
                choice = int(input ("Enter choice:-"))
                if choice >= 1 and choice <=4:
                    break
                else:
                    print("Enter a number between 1 and 4")
                    continue
            except:
                print("Wrong input")
                continue

    print("Processing....")
    time.sleep(2)

    #adding data to employee database
    employee.append(name)
    employee.append(age)
    employee.append(salary)
    employee.append(id)

    #adding employee to database
    database.append(employee)
    print("Done")
    time.sleep(1)




def read_employee():
    print(database)


def update_employee():
    name = input("Enter name:-")
    for i in database:
        if name == i[0]:
            correct = int(input("Please enter what to update:- \n"
                                "1. name\n"
                                "2. age\n"
                                "3. salary\n"
                                "4. id\n"))
            if correct == 1:
                update_name = input("Enter name:-")
                database [0][0] = update_name
                print("done!!")
                print(i)

    print("update")


def delete_employee():
    pass

def main():
    while True:
        #this is a software to CRUD - Create, Read, Update, Delete 

        print("\n\t\tWellcome to my software")
        print("1. Create an Employee\n"
              "2. Read Employee data\n"
              "3. Update Employee Info\n"
              "4. Delete Employee\n"
              "5. Exit")
    
    
        choice = int(input("Enter choice:-"))
        if choice == 1:
            create_employee()
            continue
        if choice == 2: 
           read_employee()
           continue
        if choice == 3:
           update_employee()
           continue
        if choice == 4:
           delete_employee()
           continue
        if choice == 5:
            print("Thank you!!")
            time.sleep(1)
            break

main()
