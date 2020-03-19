
import random
a=[]
found =False
for i in range (0,32):
    a.append(random.randint(5,10))    
    print(a[i],"",end="")
    if a[i]<0:
        found= True
print()

if found:
    print ("Была отрицательная температура")
else:
    print ("Небыло отрицательной температуры")