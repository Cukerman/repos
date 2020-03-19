n=int(input("Введите размер массива "))
import random
a=[]
found =False
for i in range (0,n):
    a.append(random.randint(1,10))    
    print(a[i],"",end="")
print()
#for j in range (0,len(a)) :
found = True
while found:
    found = False
    for i in range (0,len(a)-1):   
        if a[i]>a[i+1]:
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
            found = True


for i in range (0,len(a)):
    print(a[i],"",end="")
print()