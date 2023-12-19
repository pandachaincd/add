from typing import Any

print("from class1")

class Customer:

    def __init__(self, First_Name, Last_Name, Age, Phone_Number, Acc_Number, balance) -> None:
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Age = Age
        self.Phone_Number = Phone_Number
        self.Acc_Number = Acc_Number
        self.balance = balance
    

    # getter and setter 
    def get_First_Name(self):
        return self.First_Name
    def get_Last_Name(self):
        return self.Last_Name
    def get_Age(self):
        return self.Age
    def get_Phone_Number(self):
        return self.Phone_Number
    def get_Acc_Number(self):
        return self.Acc_Number
    def get_balance(self):
        return self.balance
    


    def set_First_Name(self, newval):
        self.First_Name = newval
    def set_Last_Name(self, newval):
        self.Last_Name = newval
    def set_Age(self,newval):
        self.Age = newval
    def set_Phone_Number(self, newval):
        self.Phone_Number = newval
    def set_Acc_number(self, newval):
        self.Acc_Number = newval
    def set_balance(self, newVal):
        self.balance = newVal
        

    def info(self):
        print(f"Balance {self.balance}\n Account number: {self.Acc_Number}")
    




