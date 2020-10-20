n = int(input("введите число"))
    
for i in range(1,n+1):
    if i>1 :   
        print (i)
    else:
        for i in range (n,0,-1):
            print (i)