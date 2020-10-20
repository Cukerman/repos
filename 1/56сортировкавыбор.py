n=int(input("Введите размер массива "))
import random
a=[]
found =False
for i in range (0,n):
    a.append(random.randint(1,10))    
    print(a[i],"",end="")
print()

for i in range(0,len(a)):
    c=a[i]
    for j in range(i+1,len(a)):   
        if c>a[j]:
            c=a[j]
            k=j      
    if c!=a[i]:
        a[k]=a[i]
        a[i]=c       



for i in range (0,len(a)):
    print(a[i],"",end="")
print()