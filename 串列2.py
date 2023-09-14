a=[1,23,5,17,19]
b=[2,34,6,8,16,18]
c=a+b
for i in range(len(c)):
    print('%3d'%(c[i]),end=',')
print()
d=[]
for i in range(len(c)):
    if(c[i]>=10):
        d.append(c[i])
for i in range(len(d)):
    print('%3d'%(d[i]),end=',')
