n = int(input("Введите число "))
x=1
p=1
c=0    
for i in range (1,n):
    x = 0
    x = p + c 
    c = p
    p = x
print (x) 
