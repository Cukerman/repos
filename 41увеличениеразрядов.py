def one(n):
    if n==0:
        return    
    one(n//10)
    print(((n%10)+1)%10,end="")   


c=int(input("Введите число "))
one(c) 
print()           
   