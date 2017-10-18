
def fib(n):
    x, y = 0, 1
    for i in (2,n): x, y= y, x + y
    print y


fib(8)
