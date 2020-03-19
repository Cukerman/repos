def ght(n,k):
    k+=n%10
    n=n//10
    if n!=0:
        k*=10
        return ght(n,k)
    else:
        return k  

c=int(input("Введите число "))
x=ght(c,0) 
print(x)          
