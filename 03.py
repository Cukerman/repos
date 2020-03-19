n = int(input("введите число"))
for i in range(1,n+1):
    if i == n: 
        print (i)
    else:
        print (f"{i}, ", end="")