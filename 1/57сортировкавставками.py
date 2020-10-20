n=int(input("Введите размер массива "))
import random
a=[]

for i in range (0,n):
    a.append(random.randint(1,10))    
    print(a[i],"",end="")
print()
for i in range(1,len(a)):
    while a[i]<a[i-1] and i>0:
        k=a[i]
        a[i]=a[i-1]
        a[i-1]=k
        i-=1


for i in range (0,len(a)):
    print(a[i],"",end="")
print()