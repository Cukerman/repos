n = int(input("введите число"))
for i in range (0,n):
    for j in range (0,n):
        if ((i>=n-(j+1)) and i<=j)or (i<=n-(j+1)) and i>=j  :
            print("*",end="")
        else:
            print(".",end="")   
    print ()            