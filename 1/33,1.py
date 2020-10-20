def fact (x):
    r = 1
    for i in range(1,x+1):
        r *= i
    return r       
n=int(input("введите большее число "))
m=int(input("введите меньшее число "))
while n < m :
    print("Ошибка")
    n=int(input("введите большее число "))
    m=int(input("введите меньшее число "))
m = fact(n) / (fact(m) * fact(n-m))
print(m)  