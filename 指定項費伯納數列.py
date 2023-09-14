print('34塗蒼璿')
while 1:
    user=int(input("求出第n項費伯納數列:"))
    if(user==0):
        break
    if(user==1 or user==2):
        print(user-1)
        continue
    a=0
    b=1
    for i in range(1,user-1):
        c=a+b
        a=b
        b=c
    print(b)