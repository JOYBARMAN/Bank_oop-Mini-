class User():
    def __init__(self,name,age,gender,phone):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone=phone

    def show_user(self):
        print("User Information")
        print("Name ::",self.name)
        print("Age ::",self.age)
        print("Gender ::",self.gender)
        print("Phone ::",self.phone)

class Bank(User):
    def __init__(self,name,age,gender,phone):
        super().__init__(name,age,gender,phone)
        self.balance=0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.amount+self.balance
        print(self.amount,"Taka is Deposited in Your Acoount . Current Balance is -",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if(self.balance>self.amount):
            self.balance = self.balance - self.amount
            if(self.balance>100):
                print(self.amount,"Taka Withdraw from your account & your main balance is ",self.balance)
            else:
                print("You Must Have at least 100 Tk to main balance")
        else:
            print("Insufficent Fund")

    def show_balance(self):
        print("Your Current Balance is ",self.balance)


user=Bank("Joy Barman",25,"Male","01781239312")
# user.show_user()
user.deposit(10000)
user.withdraw(9899)
user.show_balance()