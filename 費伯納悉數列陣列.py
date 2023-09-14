a=[0]*100
a[0]=0
a[1]=1
for i in range(2,50):
    a[i]=a[i-1]+a[i-2]
while 1:
    user=int(input("第幾項費伯納序列"))
    print("第%d像費伯納續列為%d"%(user,a[user-1]))
