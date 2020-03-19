n = int(input("Введите число  "))
ones=['','one','two','three','four','fife','six','seven','eight','nine']
ens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
orde=['hundred','thousand','million','billion']
a=[]
i=1
def gt (n) :           
    if n%100<10:    
        a.append(ones[n%10])
    elif 9<n%100<20:
        a.append(teens[n%10])
    else:
        a.append(ones[n%10])
    n//=10
    if n>0:
        a.append(ens[n%10])
        n//=10
    if n>0:    
        if n%10!=0:
            a.append(orde[0])
        a.append(ones[n%10])
        n//=10
    return n
if n==0:
    print('zero') 
else:
    if n<0:
        print('minus','',end='')
        n=-n
    n=gt(n)
    while n>0:    
        if n%1000>0:
            a.append(orde[i])
        n=gt(n)
        i+=1    
    for i in range (len(a)-1,-1,-1):    
        print(a[i],end='')
        if a[i]!='':
            print(' ',end='')           
    print()
