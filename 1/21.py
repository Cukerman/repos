n = int(input("введите число"))
while n%2==0:
    n = int(input("Введите нечетное число"))
for u in range(n,0,-2):
    for i in range ((n-u)//2):
        print (" ",end="")
    for i in range (u):
        print ("*",end="")
    print ()        
for u in range (3,n+1,2):
    for i in range ((n-u)//2):
        print (" ",end="")
    for i in range (u):
        print ("*",end="")
    print ()       