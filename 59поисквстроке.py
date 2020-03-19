a=input('Введите строку ')
n=input('Введите символ ')
found=False
for i in range (len(a)):
    if a[i]==n:
        found=True
        break
        
if not found:
    print ('Символа нету')  
else:
    print(i)
