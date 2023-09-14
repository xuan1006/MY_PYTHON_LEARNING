#印出2~1000的質數
#0,1,1,2,3,5,8,13
#a,b
#c=a+b
#印出c
#a   b
print('34塗蒼璿')
a=0
b=1
count=0
n=int(input('加到第幾個'))
print('%3d%3d'%(a,b),end=',')
while(b<1000):
    c=a+b
    print('%3d'%(c),end=',')
    a=b
    b=c
