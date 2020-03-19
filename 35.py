import random
x=random.randint(1,100)
n=int(input("Введите число "))
i=1
while n!=x:
    i+=1
    if n>x:
        print("Ваше число больше")
    else:
        print("Ваше число меньше")
    n=int(input("Введите число "))
print (i)