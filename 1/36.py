def fib(x):
    p=1
    c=0    
    for i in range (1,x):
        k = 0
        k = p + c 
        c = p
        p = k
    return p 
n=int(input("Введите номер числа "))
print(fib(n))