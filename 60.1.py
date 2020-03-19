a='а роза упала на лапу азора'

found=False
def pol (c,k):
    if c<k:
        if a[c]==' ':
            return pol(c+1,k)
        elif a[k]==' ':
            return pol(c,k-1)
        else:
            if a[c]!=a[k]:    
                return 'Нет'        
        return pol(c+1,k-1)
    else:
        return 'Да'
print(pol(0,len(a)-1))

