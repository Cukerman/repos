import random
n=int(input('Введите кол-во команд '))
m=int(input('Введите кол-во соревн '))
a=[0]
x=0
k=0
c=0
for i in range(1,n+1):
    a.append([])
    for j in range(0,m):
        a[i].append(random.randint(1,10))
        k+=a[i][j]
    if x<k :
        x=k
        c=i 
    k=0   
    print('Команда',i,a[i])    

#for i in range(1,n+1):    
 #   for j in range (0,m):
    #    k=k+a[i][j]
   # if x<k and i!=c:
  #      x=k
 #       k=0
#        c=i
print ('Победила команда',c)
