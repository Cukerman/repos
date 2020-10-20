def ght(n):
    if n==0:
        return
    print(n%10,end="")
    ght(n//10)
    
    
c=int(input("Введите число "))
ght(c)            
print()