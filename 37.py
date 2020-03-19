def clock(n,s):
    for u in range(n,0,-2):
        for i in range (s+((n-u)//2)):
            print (" ",end="")
        for i in range (u):
            print ("*",end="")
        print ()        
    for u in range (3,n+1,2):
        for i in range (s+((n-u)//2)):
            print (" ",end="")
        for i in range (u):
            print ("*",end="")
        print()    
q=int(input("Введите номер числа "))   
c=q
k=0
while q > 1:
    clock(q,k)
    q-=2
    k+=1
while q<=c :
    clock(q,k)
    q+=2
    k-=1