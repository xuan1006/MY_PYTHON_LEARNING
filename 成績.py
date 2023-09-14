import numpy as np
s=100
a=[]
b=[]
while(s!=-1):
    s=int(input("輸入分數，-1結束"))
    if(s==-1):
        break
    a.append(s)
    if(s<60):
        b.append("不及格")
    if(60<=s<80):
        b.append("乙")
    if(s>=80):
        b.append("甲")
print("編號\t成績\t等第")
for i in range(0,len(a)):
    print("%d\t%d\t%s" %((i+1),a[i],b[i]))
print("標準差:%6.2f"%(np.std(a)))
