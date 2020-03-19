n=int(input("введите большее число "))
m=int(input("введите меньшее число "))
while n < m :
    print("Ошибка")
    n=int(input("введите большее число "))
    m=int(input("введите меньшее число "))
p=1
for i in range (1,n+1):
    p *= i    
q = p
p = 1
for i in range (1,m+1):
    p *= i
w = p
p = 1
k = n-m
for i in range (1,k+1):
    p *= i             
e = p
print(q/(w*e))