#n = int(input("Введите число"))
#m = 0
#while n!=0:
#    m += n % 10
#    n = n // 10
#print (m)    
def qwe(n):
    if n==0:
        return 0
    return qwe(n//10)+n%10
        
     


c=int(input("Введите число "))
print(qwe(c) ) 