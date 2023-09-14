list=[[0]*4 for i in range(4)]
count=1
for i in range(0,4):
    for j in range(0,4):
        list[i][j]=count
        count+=1
for i in range(0,4):
    print(list[i])