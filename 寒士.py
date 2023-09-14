def nby(n):
    a=0
    for i in range(1,n+1):
        if (i%2==0):
            a-=(1/(i*(i+1)))
        else:
            a+=(1/(i*(i+1)))
    return a



n=int(input("輸入一個數"))
ans=nby(n)
print("%f6"%(ans))
