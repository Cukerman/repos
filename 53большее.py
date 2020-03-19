n=int(input("Введите размер массива "))
import random
a=[]
for i in range (0,n):
    a.append(random.randint(-5,10))    
    print(a[i])

c=0
for i in range (len(a)):
    if a[i]>a[c]:
        
        c=i
print("Наибольшее число в массиве ",a[c])
print("Номер наибольшего числа в массиве ",c)