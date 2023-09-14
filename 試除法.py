# 請使用「試除法」找出100到200之間所有的質數，
# 並計算總共有多少個。所謂的「試除法」，是假設被測試的自然數為n，
# 然後逐一測試2與根號n之間的整數，確保它們無一能整除n，此時n即為質數。
counts=0
bool1=True
for i in range(100, 200+1):
    bool1=True
    for j in range(2, int(i**0.5)+1):
        if(i%j==0):
            bool1=False
            break
    if(bool1):
        print(i,"is prime num!")
    counts+=1