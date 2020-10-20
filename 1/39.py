def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n
c=int(input("Введите число ")) 
print(fact(c))       