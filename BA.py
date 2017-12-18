class Account:
    count = 0
    def __init__(self, own):
        self.own =  own
        self.money = 0
        number = Account.count
        Account.count+=1

    def withdraw(self, w):
        self.money = self.money - w

    def deposit(self, d):
        self.money = self.money + d



    def __str__(self):
        return "%s 's bank account(%d) has $ %.2f in their account"%(self.own, Account.count, self.money)

x = 0
end = 1
while end == 1:
    x = raw_input("Do you want to make a bank account(1), withdraw from your bank account(2), or deposit money into your bank account(3), view account info(4) or exit the program(5)?")
    if x == "1":
        own = raw_input("What is your name?")
        account1 = Account(own)
        print account1
        print "_______________"

    if x == "2":
        w = input("How much money do you want to take out? (please omit the dollar sign)")
        account1.withdraw(w)

    if x == "3":
        d = input("How much do you want to deposit?")
        account1.deposit(d)

    if x == "4":
        print "Your information:"
        print account1

    if x == "5":
        z = raw_input("Do you want to leave the program? (y? or n?)")
        if z == "y":
            end = 2
