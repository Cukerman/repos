a=[1,2,3,5,6,7,9,11,12,14]
n=int(input("Введите число "))
k=len(a)//2
found=True
r=len(a)
f=1
x=r
while r>1 and len(a)>k>-1:
    r/=2
    c=x-k+1
    c//=2  
    if a[k]==n : 
        found=False
        break 
    elif a[k] > n:       
        x=k
        k-=c
        
    elif a[k] < n :        
        
        k+=c      
    f+=1    
        
if found:
    print("Такого числа нет")
else:
    print(k)
    print(f)