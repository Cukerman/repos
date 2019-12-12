n = int(input("введите число"))
    
for u in range(n,0,-1):
    for i in range (u-1):
        print ("*",end="")
    print ("*")        
for u in range(1,n):
    for i in range (u):
        print ("*",end="")
    print ("*")        
          