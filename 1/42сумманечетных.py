def sum(n):
    if n%2!=1:
        n-=1
    if n==1 :
        return 1
    return sum(n-2)+n
       
c=int(input("Введите число "))

print(sum(c) ) 
