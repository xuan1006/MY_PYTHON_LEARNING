scores = [90,59,78,71,39,0,19,85,77,84,91,98,38,66,65,88,63,85,18,0]
freq=[0]*5
for score in scores:
    if(score<20):
        freq[0]+=1
    elif(score<40):
        freq[1]+=1
    elif(score<60):
        freq[2]+=1
    elif(score<80):
        freq[3]+=1
    else:
        freq[4]+=1
print('人數分布:',freq)