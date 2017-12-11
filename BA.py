count = 0

class Account:

    def __init__(self, money, own):
        self.money = money
        self.own =  own

    def deposit(self):
        d = raw_input("How much do you want to deposit?")
        self.money + d = self.money

    def withdraw(self):
        w = raw_input("How much money do you want to take out? (please omit the dollar sign)")
        self.money + w = money

    def balance(self):
        print "Your acccount balance is:"
        print "$",self.money

    def num(self):
        Account.count+=1
        number = Account.count
        print number

end = 1
while end == 1:
    x =raw_input("Do you want to make a bank account(1), withdraw from your bank account(2), or deposit money into your bank account(3)?")
    if x == 1:
        own = raw_input("What is your name? ")
        money = 0
        sid = 0
        account1 = Account(own)
        student1.num()
        print "_______________"
    if x == 2:
        n = raw_input("Do you want to see your account information? (y? or n?)")
        if n == "y":
            print "Your information:"
            print account1.own
            print account1.balance

        else:
            z = raw_input("Do you want to leave the program? (y? or n?)")
            if z == "y":
                end = 2
