a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
b=0
for i in range(0,len(a)):
    print(a[i],end=",")

print()
for i in range(1,16,2):
    print(a[i],end=",")
print()
for i in range(len(a)):
    b+=(a[i])
print(b)

