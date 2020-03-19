n=int(input("Введите размер массива "))
import random
a=[]
for i in range (0,n):
    a.append(random.randint(-5,10))    
    print(a[i])
k=int(input("Введите число "))
found = False
for i in range (0,n):
    if a[i]==k:
        found = True
        print("Номер числа в массиве ",i)
        break
if not found:
    print("Такого числа нет в массиве ")         