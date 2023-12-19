
class TELE:
    def __init__(self, first_name, last_name, age, phone_number, balance, internet, voice, sms ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.balance = balance
        self.internet = internet
        self.voice = voice
        self.sms = sms


    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_age(self):
        return self.age
    def get_phone_number (self):
        return self.phone_number
    def get_balance (self):
        return self.balance
    def get_internet (self):
        return self.internet
    def get_voice(self):
        return self.voice
    def get_sms (self):
        return self.sms
    

    def set_first_name(self, newvalue):
        self.first_name = newvalue
    def set_last_name(self, newvalue):
        self.last_name = newvalue
    def set_age(self, newvalue):
        self.age = newvalue
    def set_phone_number(self, newvalue):
        self.phone_number = newvalue
    def set_balance(self, newvalue):
        self.balance = newvalue
    def set_internet(self, newvalue):
        self.internet = newvalue
    def set_voice(self, newvalue):
        self.voice = newvalue
    def set_sms(self, newvalue):
        self.sms = newvalue