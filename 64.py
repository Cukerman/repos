a=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def tre():
    for i in range (0,3)    :
        print('+-+-+-+')
        for j in range (0,3) :   
            print('|',end='')
            print(a[i][j],end='')
        print('|')
    print('+-+-+-+')    
tre()
def x():
    found=True
    while found:            
        i=int(input('Введите строку '))
        j=int(input('Введите столбец '))
        if 0<i<4 and 0<j<4:
            if a[i-1][j-1]==' '  :
                a[i-1][j-1]='X'
                found=False
            else:
                print('Клетка уже занята')
        else :
            print('Ошибка')
def o():
    found=True
    while found:            
        i=int(input('Введите строку '))
        j=int(input('Введите столбец '))
        if 0<i<4 and 0<j<4:
            if a[i-1][j-1]==' '  :
                a[i-1][j-1]='O'
                found=False
            else:
                print('Клетка уже занята')
        else :
            print('Ошибка')


c=9
while c>0  :  
    print('Ходит Х')
    x()
    tre()
    for i in range (0,3):
        k=0
        c=0
        for j in range (0,3):        
            if a[i][j]=='X':
                k+=1
            if a[j][i]=='X'
                c+=1            
            if k==3 or c==3:                
                print ('Победил X')
                c=0
                break    
    di()
    if c>0:        
        print('Ходит O')
        o()
        tre()
        for i in range (0,3):
            k=0
            c=0
            for j in range (0,3):        
                if a[i][j]=='O':
                    k+=1
                if a[j][i]=='O'
                    c+=1
                if k==3 or c==3:                
                    print ('Победил O')
                    c=0
                    break
    

    c-=1