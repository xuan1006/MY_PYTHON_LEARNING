def nby(n):
    for i in range(1,n):
        if (n%2==0):
            a+=1/n*(n+1)-1/n*(n+1)*(n+2)
        else:
            a=-(1/n*(n+1))-1/n*(n+1)*(n+2)
    return a



num=int(input("輸入一個數"))
ans=(nby,num)
print("%f6.2"%(nby))


