n = int(input("Введите число  "))
ones=['','one','two','three','four','fife','six','seven','eight','nine']
ens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
orde=['','hundred','thousand','million','billion']
a=[]
def qwe (n, i=2):
    if n==0:
        print("zero")
        return
    elif n<0:
        print("minus ",end='')
        n=-n
    if n%100<10 and n%10!=0:    
        a.insert(0,ones[n%10])
    elif 9<n%100<20 :
        a.insert(0,teens[n%10])
    else:
        if n%10!=0:
            a.insert(0,ones[n%10])
    n//=10
    if n>0 and n%10>1 :
        a.insert(0,ens[n%10])
    n//=10
    if n>0:    
        if n%10!=0:
            a.insert(0,orde[1])
            a.insert(0,ones[n%10])
        n//=10
    while n>0:    
        if n%1000>0 :
            a.insert(0,orde[i])
        i+=1
        return qwe(n,i)
    print(*a)    # " ".join(a)
qwe(n)        
    

#for i in a:
#    s += i + ' '
#print(s)
