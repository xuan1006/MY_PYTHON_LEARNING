def fact(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    return p
a=int(input('階乘'))
print("%d"%(fact(a)))
