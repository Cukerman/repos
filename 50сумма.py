n=int(input("Введите размер массива "))
a=[]
for i in range (0,n):
    a.append(int(input("Введите элемент массива ")))    
a.append(0)
for i in range (0,n):
    a[n]+=a[i]
    print(i,end="")
    print(".",a[i])
print("Сумма эл-тов массива =",a[n])


