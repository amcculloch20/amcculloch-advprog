x = 0
A =[]
def pal(x):
    strx = str(x)
    y = strx[::-1]
    if strx == y:
        return True
         
pal(x)


def main():
    for i in range(100,1000):
        for j in range(100,1000):
            x =j*i
            if pal(x):
                A.append(x)
    A.sort()
    A.reverse()
    print A[0]

main()
