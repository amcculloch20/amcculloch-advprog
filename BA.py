class Account:
    count = 0
    def __init__(self, own, money,d,w):
        self.own =  own
        self.money = money
        self.d = d
        self.w = w

    def deposit(self):
        self.money = self.money + self.d

    def withdraw(self):
        self.money = self.money + self.w

    def balance(self):
        print "Your acccount balance is:"
        print "$",self.money

    def num(self):
        Account.count+=1
        number = Account.count
        print "Account number is:",number

    def disp(self):
        print self.own
        print "$", self.money,"in your account"

sid = 0
x = 0
end = 1
while end == 1:
    x = raw_input("Do you want to make a bank account(1), withdraw from your bank account(2), or deposit money into your bank account(3), view account info(4) or exit the program(5)?")
    if x == "1":
        own = raw_input("What is your name?")
        money = 0
        account1 = Account(own,0,0,0)
        account1.num()
        print "_______________"

    if x == "2":
        w = input("How much money do you want to take out? (please omit the dollar sign)")
        account1.withdraw()

    if x == "3":
        n = input("How much do you want to deposit?")
        account1.deposit()

    if x == "4":
        n = raw_input("Do you want to see your account information? (y? or n?)")
        if n == "y":
            print "Your information:"
            print account1.disp()

    if x == "5":
        z = raw_input("Do you want to leave the program? (y? or n?)")
        if z == "y":
            end = 2
