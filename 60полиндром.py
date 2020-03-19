#a=input('Введите строку ')
a='а роза упала на лапу азора'
found=False
i=0
c=len(a)-1
k=0
while 0<(c-i) :  

    while a[i]==' ':        
        i+=1
                    
    while a[c]==" ":        
        c-=1
                
    if a[i]!=a[c]:
        found=True
        break  
    i+=1
    c-=1        
    
if found:
    print('Нет')
else:
    print("Да")

            
            
