
from newa import TELE

def check_balance(TELE):
    print("Your current balance is: ", TELE.get_balance())


def Transfer_balance(TELE):
    print("Trans working")
    # No to transfer 
    while True:
        trans_phone = input("Enter phone number to transfer: _ ")

        trans_data = [data for data in database if data.phone_number == trans_phone]
        customer2 = trans_data[0]
        
        if len(trans_data) == 0:
            print("Wrong input")
            continue
        else:
            break
        
                 

    # amount to transfer

    while True:
        amount = int(input("Enter Transfer amount: "))
        print( 
            "owner: - ", TELE.get_balance(),
            "\nother guy: - ", customer2.get_balance()
        )
        # check if amount is less than balance 
        if amount >= TELE.get_balance():
            print("Your balance is insufficent!!")
            continue
        
        
        if amount < TELE.get_balance():
            # subtract amount form balance and add amount to transfer account
            TELE.set_balance(amount - TELE.get_balance())
            # setting balance of the transferee
            customer2.set_balance(amount + customer2.get_balance())

            print( 
            "owner: - ", TELE.get_balance(),
            "\nother guy: - ", customer2.get_balance()
        )
            break
    
balance_notify = "Dear customer, you have provides"
    

    # print success and show balance 

def buy_package(TELE):
    print("buy package is working")
    print(
        "1. buy voice package\n"
        "2. buy internet package\n"
    )
    package = int(input(""))
    if package == 1:
        print("1. daily\n"
              "2. weekly\n"
              "3. monthly\n"
              ""
              )
        choice = int(input(""))
        if choice == 1:
            print("1. 3 birr for 15min\n"
                    "2. 5birr for 30 min\n"
              "3. 15 birr for 80min\n"
              )
            choice1 = int(input(""))
            if choice1 == 1:
               TELE.set_balance( TELE.get_balance() - 3)
               TELE.set_voice(TELE.get_voice() + 15)
               print(balance_notify, TELE.get_balance(), "Your voice is ", TELE.get_voice() )
            
            elif choice1 == 2:
                TELE.set_balance( TELE.get_balance() - 5)
                TELE.get_voice( TELE.get_voice() + 30)
                print(balance_notify, TELE.get_balance(), "your voice is", TELE.get_voice() )

            
            elif choice1 == 3:
                TELE.set_balance( TELE.get_balance() - 15)
                TELE.set_voice( TELE.get_voice() + 80)

        
        if choice == 2:
            print("1. 25 birr for 120min\n"
                "2. 35 birr for 180min\n"
                "3. 50 birr for 250min\n"
            )
            choice01 = int(input(""))
            if choice01 == 1:
                TELE.set_balance( TELE.get_balance() -25)
                TELE.get_voice( TELE.get_voice() +120)
                print(balance_notify, TELE.get_balance(), "your voice is", TELE.get_voice())
            
            elif choice01 == 2:
                TELE.set_balance( TELE.get_balance() -35)
                TELE.set_voice( TELE.get_voice() +180)
            
            elif choice01 == 3:
                TELE.set_balance( TELE.get_balance() - 50)
                TELE.set_voice( TELE.get_voice() +250)
                print(balance_notify, TELE.get_balance(), "your voice is", TELE.get_voice())
                
        if choice == 3:
            print("1. 100 birr for 550min\n"
                    "2. 150 birr for 685min\n"
                    "3. 200 birr for 1250min\n"
                    )
            choice12 = int(input(""))
            if choice12 == 1:
                TELE.set_balance( TELE.get_balance() -100)
                TELE.set_voice(TELE.get_voice() +550)
                print(balance_notify, TELE.get_balance(),)
            


def check_phone_number(TELE):
    print("Your phone number is:- ", TELE.get_phone_number())

def call_center():
    print("getting call center")

if __name__ == "__main__":
    database = []
    database.append(TELE("a", "b", 23, "+251911111111", 1000, 0, 0, 0))
    database.append(TELE("c", "d", 23, "+251911111112", 1000, 0, 0, 0))
    customer = TELE("", "", "", "", "", "", "", "")
    # get the phone number 
    while True:
        try:
            phone_entered = input("Enter phone_number:-")
        except:
            print()

        info = [data for data in database if data.phone_number == phone_entered]

        if len(info) == 0:
            print("Wrong input")
            continue
        else:
            break
    
    customer = info[0]

    # Know who the person is and greet him
    
    print("Hi", customer.first_name)
    
    while True:
        # first show options of *80 # 
        print("Please call: \n\t*804#,*805#,*806#,*999#,*994#,*111#")
        call = input("")

        # write the functions with conditional decision making
        if call == "*804#":
            check_balance(customer)
            continue
        elif call == "*806#":
            Transfer_balance(customer)
            continue
        elif call == "*999#":
            buy_package(customer)
            continue
        elif call == "*111#":
            check_phone_number(customer)
            continue
        elif call == "*994#":
            call_center(customer)
            continue
        else:
            print("wrong mms code!!")