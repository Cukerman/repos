import random
n=int(input('Введите кол-во команд '))
m=int(input('Введите кол-во соревн '))
a=[[]]
x=0
k=0
c=0
s=[]

for i in range(0,n):
    a.append([])    
    for j in range(0,m):
        a[i].append(random.randint(1,10))      
        k=k+a[i][j]
    
    a[i].append(k)
    k=0
    print('Команда',i+1,a[i])

while c<n :
    
    for i in range(0,n):
        if k<a[i][m]:
            k=a[i][m]
            
            x=i             
    s.append(x+1)
    s.append(k)
    k=0
    a[x][m]=0        
    c+=1
       
   

for i in range (0,len(s),2):
    print(s[i],s[i+1])        





        



    
        
    


