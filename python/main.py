import time
database = [["Name", "Age", "Salary", "ID"]]

def create_employee():
    employee = []
    print("\n\tCreating An Employee\n"
          "\tPlease enter the following Information\n")
    name = input("Enter Name: - ")
    age = int(input("Enter age: - "))
    salary = int(input("Enter salary: - "))
    id = int(input("Enter id: - "))

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
    print("update")
    

def delete_employee():
    print("delete")


def main():
    while True:
        # this is a software to CRUD - Create, Read, Update, Delete
        print("\n\t\tWellcome to my SOftware!")
        print("1. Create an Employee\n"
            "2. Read Employee Data\n"
            "3. Update Employee INfo\n"
            "4. Delete Employee\n"
            "5. Exit")
        
        choice = int(input("Enter Choice: - "))
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
            print("Thank you for using my app!!")
            time.sleep(1)
            break




main()