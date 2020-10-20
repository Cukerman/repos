a=[5,5,5,5,5,5]


for i in range (0,len(a)):
    if a[i]== 5: 
        c = False
    elif a[i]==2:
        c= True
        print("Двоечник")
        break
    elif a[i]==3 or a[i]==4 :
        c= True
        print("Обычный")
        break
if not c:
    print("Отличник")    

     
